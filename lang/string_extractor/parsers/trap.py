from ..write_text import write_text


def parse_trap(json, origin):
    id = json["id"]

    if "name" in json:
        write_text(json["name"], origin, comment="Name of a trap")
    if "vehicle_data" in json and "sound" in json["vehicle_data"]:
        write_text(json["vehicle_data"]["sound"], origin,
                   comment="Trap-vehicle collision message for trap '{}'"
                   .format(id))

    for key in ["memorial_male", "memorial_female"]:
        if key in json:
            write_text(json[key], origin,
                       comment="Memorial message of trap \"{}\"".format(id))

    if "trigger_message_u" in json:
        write_text(json["trigger_message_u"], origin,
                   comment="Message when player triggers trap \"{}\""
                   .format(id))

    if "trigger_message_npc" in json:
        write_text(json["trigger_message_npc"], origin,
                   comment="Message when NPC triggers trap \"{}\""
                   .format(id))
