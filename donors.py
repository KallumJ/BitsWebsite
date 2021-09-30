from player_data_api import get_list_of_vip_uuids, get_effective_name_from_uuid


def get_donor_player_list():
    donors = []

    try:
        uuids = get_list_of_vip_uuids()

        # Kall, Nex, and our alts
        blacklist_uuids = ["b9be5135-fe8c-4a34-9e63-ffeef0fc80fb",
                           "cac04f5f-726f-4192-8290-24bdd9e7c9aa",
                           "90fd7b3f-239f-4ba4-809c-427081ebfa4e",
                           "0d594da7-6b81-463e-a0a7-d21c2e6b76f5"]

        for uuid in uuids:
            # If player is not blacklisted
            if not blacklist_uuids.__contains__(uuid):
                # Add player to list of donors
                player_dict = {"username": get_effective_name_from_uuid(uuid),
                               "headImage": "https://visage.surgeplay.com/head/" + uuid}

                donors.append(player_dict)
        return donors
    except Exception as e:
        print("A problem occurred accessing the donors list. " + str(e))
        return None
