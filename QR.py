class QrScan:
    source = "this_vac_info.txt"
    destination = "this_vac_info2.txt"

    def capture_qr(self):
        origin_qr = open(self.source, 'rt')
        self.origin_qr_decrypted = origin_qr.read()
        origin_qr.close()

    def process_qr(self):
        destination_qr = open(self.destination, 'wt')
        destination_qr.write(self.origin_qr_decrypted)
        destination_qr.close()

    def verify_qr_scan(self):
        origin = open(self.source, 'rt')
        origin_reader = origin.read()
        origin.close()
        destination = open(self.destination, 'rt')
        destination_reader = destination.read()
        destination.close()
        if origin_reader == destination_reader:
            print(destination_reader, "\n")
            print("QR Code scan was successful")
        else:
            print("Failed to Scan QR code")

    @staticmethod
    def execute_qr_scan():
        QrScan.capture_qr(QrScan)
        QrScan.process_qr(QrScan)
        QrScan.verify_qr_scan(QrScan)


QrScan.execute_qr_scan()
