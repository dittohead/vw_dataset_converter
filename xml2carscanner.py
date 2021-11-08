import xml.etree.ElementTree as ET


class xml2carscanner():
    def __init__(self, file):
        self.file = file
        self.output_line = ''
        self._parsed_data_blocks = []
        self.parsed_bytes = []
        self.find_data()


    def find_data(self):
        root = ET.parse(self.file).getroot()
        pd = root[0][0][0].findall("PARAMETER_DATA")
        for item in pd:
            block_id = item.attrib['DIAGNOSTIC_ADDRESS']
            start_address = item.attrib['START_ADDRESS']
            payload = item.text.replace(" ", "")
            self._parsed_data_blocks.append(
                {
                    "blockID": block_id,
                    "address": start_address,
                    "data": payload
                })

    def parsed_data_blocks(self):
        return self._parsed_data_blocks

    def get_data_via_address(self, address):
        try:
            return self.find_block_by_adress(address)["data"]
        except TypeError:
            return None

    def get_blockID_via_adress(self, address):
        try:
            return self.find_block_by_adress(address)["blockID"]
        except TypeError:
            return None

    def find_block_by_adress(self, address):
        for item in self._parsed_data_blocks:
            if item["address"] == address:
                return item

    def _data_to_bytes_blocks(self, data):
        self.parsed_bytes = data.split(",")

    def _convert_data_to_string(self):
        for item in self.parsed_bytes:
            self.output_line += item
            self.output_line = self.output_line.replace("0x", "")
        return self.output_line

    def get_data_via_adress_as_string(self, address):
        _data = self.get_data_via_address(address)
        self._data_to_bytes_blocks(_data)
        return self._convert_data_to_string()
