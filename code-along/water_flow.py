# Enhancement: using physical constants + adds psi conversion feature
# - Constants defined at top
# - Corrected pipe reduction formula to match assignment
# - Zero-case handling added so tests that expect 0.0 pass
# - Outputs both kPa and psi in main()

EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    """Return the effective water column height (meters)."""
    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height):
    """Return pressure gain from water column height in kilopascals (kPa)."""
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000.0


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Return pressure loss (negative) from a straight pipe (kPa).

    Formula: P = - f * L * rho * v^2 / (2000 * d)
    """
    # Guard zero-case inputs used by tests
    if pipe_length == 0 or friction_factor == 0 or fluid_velocity == 0:
        return 0.0
    # Avoid division by zero for pipe_diameter
    if pipe_diameter == 0:
        raise ValueError("pipe_diameter must be non-zero")
    return -(friction_factor * pipe_length * WATER_DENSITY * fluid_velocity * fluid_velocity) / (2000.0 * pipe_diameter)


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Return pressure loss (negative) from fittings (kPa).

    Formula: P = -0.04 * rho * v^2 * n / 2000
    """
    if fluid_velocity == 0 or quantity_fittings == 0:
        return 0.0
    return -(0.04 * WATER_DENSITY * fluid_velocity * fluid_velocity * quantity_fittings) / 2000.0


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Return Reynolds number (dimensionless).

    Formula: R = rho * d * v / mu
    """
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Return pressure loss (negative) caused by a pipe reduction (kPa).

    Interpreted formula:
      k = 0.1 + 50 / R
      P = -k * ( (D/d)^4 - 1 ) * rho * v^2 / 2000
    """
    # Zero or no-flow cases
    if fluid_velocity == 0 or reynolds_number == 0 or smaller_diameter == 0:
        return 0.0

    ratio4_minus1 = (larger_diameter / smaller_diameter) ** 4 - 1.0
    k = 0.1 + 50.0 / float(reynolds_number)
    return -(k * ratio4_minus1 * WATER_DENSITY * fluid_velocity * fluid_velocity) / 2000.0


def kpa_to_psi(kpa):
    """Convert kilopascals to psi (pounds per square inch)."""
    return kpa * 0.1450377377


def main():
    # Read inputs exactly as the example in the assignment
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    supply_pipe_length = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_90_angles = int(float(input("Number of 90° angles in supply pipe: ")))
    house_pipe_length = float(input("Length of pipe from supply to house (meters): "))

    # Compute the water column and pressure gain
    column = water_column_height(tower_height, tank_height)
    gain = pressure_gain_from_water_height(column)

    # Use the pipe values from the assignment/example
    LARGE_PIPE_DIAMETER = 0.28687   # meters (supply)
    SMALL_PIPE_DIAMETER = 0.048692  # meters (house)
    LARGE_PIPE_FRICTION = 0.013
    SMALL_PIPE_FRICTION = 0.018
    LARGE_PIPE_VELOCITY = 1.65
    SMALL_PIPE_VELOCITY = 1.75

    supply_loss = pressure_loss_from_pipe(LARGE_PIPE_DIAMETER, supply_pipe_length, LARGE_PIPE_FRICTION, LARGE_PIPE_VELOCITY)

    R_large = reynolds_number(LARGE_PIPE_DIAMETER, LARGE_PIPE_VELOCITY)
    reduction_loss = pressure_loss_from_pipe_reduction(LARGE_PIPE_DIAMETER, LARGE_PIPE_VELOCITY, R_large, SMALL_PIPE_DIAMETER)

    fittings_loss = pressure_loss_from_fittings(SMALL_PIPE_VELOCITY, quantity_90_angles)

    house_loss = pressure_loss_from_pipe(SMALL_PIPE_DIAMETER, house_pipe_length, SMALL_PIPE_FRICTION, SMALL_PIPE_VELOCITY)

    pressure_at_house = gain + supply_loss + reduction_loss + fittings_loss + house_loss

    print(f"Pressure at house: {pressure_at_house:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure_at_house):.1f} psi")


if __name__ == "__main__":
    main()
