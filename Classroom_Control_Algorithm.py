def classroom_ventilation_control(
    occupancy: str,                  # "empty", "lecture", or "workshop"
    co2_level: int,                  # in ppm
    hallway_noise: int,             # in dB
    outside_temp: float,            # in °C
    outside_noise: int              # in dB
):
    actions = []

    if occupancy == "empty":
        actions.append("No action / Door closed")
        return actions

    if co2_level < 750:
        actions.append("CO2 below threshold: Window and Door closed")
        return actions

    # CO2 > 750 ppm — ventilation needed
    if occupancy == "lecture":
        actions.append("Signal lights RED")
        noise_threshold = 35
    elif occupancy == "workshop":
        actions.append("Signal lights ORANGE")
        noise_threshold = 50
    else:
        actions.append("No occupancy")
        return actions

    if hallway_noise < noise_threshold:
        # Low hallway noise
        if outside_temp < 26:
            if outside_noise < noise_threshold:
                actions.append("Open Window and Door")
            else:
                actions.append("Open only Door")
        else:
            actions.append("Open only Door")
    else:
        # High hallway noise
        if outside_temp < 26:
            if outside_noise < noise_threshold:
                actions.append("Open only Window")
            else:
                actions.append("Turn on Mechanical Ventilation")
        else:
            actions.append("Turn on Mechanical Ventilation")

    return actions

result = classroom_ventilation_control(
    occupancy="workshop",
    co2_level=800,
    hallway_noise=45,
    outside_temp=29,
    outside_noise=45
)
for action in result:
    print(action)
