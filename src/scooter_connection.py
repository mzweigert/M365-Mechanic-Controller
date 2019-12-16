import sys
if len(sys.argv) >= 2 and sys.argv[1] == 'fake':
    from connection_fake import XiaomiBLEBaseConnection, RecoveryEnergyMode
else:
    from py9b.connection.xiaomi_ble_connection import XiaomiBLEBaseConnection, RecoveryEnergyMode

__all__ = ['XiaomiBLEBaseConnection', 'RecoveryEnergyMode']
