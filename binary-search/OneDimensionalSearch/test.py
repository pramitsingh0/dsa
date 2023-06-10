import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    converted_object = {}
    
    # Copying deviceID and deviceType as is
    converted_object["deviceID"] = jsonObject["deviceID"]
    converted_object["deviceType"] = jsonObject["deviceType"]
    
    # Extracting timestamp as is
    converted_object["timestamp"] = jsonObject["timestamp"]
    
    # Splitting the location string and creating a location dictionary
    location_parts = jsonObject["location"].split("/")
    location = {
        "country": location_parts[0],
        "city": location_parts[1],
        "area": location_parts[2],
        "factory": location_parts[3],
        "section": location_parts[4]
    }
    converted_object["location"] = location
    
    # Creating a data dictionary with operationStatus and temp
    data = {
        "status": jsonObject["operationStatus"],
        "temperature": jsonObject["temp"]
    }
    converted_object["data"] = data
    
    return converted_object


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    converted_object = {}
    
    # Extracting device ID and type from nested "device" object
    device = jsonObject["device"]
    converted_object["deviceID"] = device["id"]
    converted_object["deviceType"] = device["type"]
    
    # Parsing the timestamp string to milliseconds
    timestamp = datetime.datetime.fromisoformat(jsonObject["timestamp"].replace("Z", "+00:00")).timestamp() * 1000
    converted_object["timestamp"] = int(timestamp)
    
    # Creating a location dictionary
    location = {
        "country": jsonObject["country"],
        "city": jsonObject["city"],
        "area": jsonObject["area"],
        "factory": jsonObject["factory"],
        "section": jsonObject["section"]
    }
    converted_object["location"] = location
    
    # Copying data as is
    converted_object["data"] = jsonObject["data"]
    
    return converted_object


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
