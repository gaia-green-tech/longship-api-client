from enum import Enum


class LocationEVSEDtoCapabilitiesItem(str, Enum):
    CHARGING_PREFERENCES_CAPABLE = "CHARGING_PREFERENCES_CAPABLE"
    CHARGING_PROFILE_CAPABLE = "CHARGING_PROFILE_CAPABLE"
    CHIP_CARD_SUPPORT = "CHIP_CARD_SUPPORT"
    CONTACTLESS_CARD_SUPPORT = "CONTACTLESS_CARD_SUPPORT"
    CREDIT_CARD_PAYABLE = "CREDIT_CARD_PAYABLE"
    DEBIT_CARD_PAYABLE = "DEBIT_CARD_PAYABLE"
    PED_TERMINAL = "PED_TERMINAL"
    REMOTE_START_STOP_CAPABLE = "REMOTE_START_STOP_CAPABLE"
    RESERVABLE = "RESERVABLE"
    RFID_READER = "RFID_READER"
    TOKEN_GROUP_CAPABLE = "TOKEN_GROUP_CAPABLE"
    UNLOCK_CAPABLE = "UNLOCK_CAPABLE"

    def __str__(self) -> str:
        return str(self.value)