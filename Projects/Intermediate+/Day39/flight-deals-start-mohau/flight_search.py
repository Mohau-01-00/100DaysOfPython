class FlightSearch:

    def __init__(self) -> None:
        pass

       

    def iata_code(self):

        iata_code="TESTING"

        return iata_code

    # API_KEY="nUj61aogX-f8do_0G2rVwAtg6nCdXymg"
    # #This class is responsible for talking to the Flight Search API.
    # pass




# This document guides you through the implementation of the Search API. This API is necessary for all of our B2B partners using a Search & Book solution and for all our partners using a Meta Search solution.

# 1 Prerequisites
# TLS protocol version 1.2 or later must be used.
# Use a proper content type in the headers for all requests to Tequila API: Content-Type: application/json
# Use your API key in the headers for all requests to Tequila API: apikey: yourapikeyvalue
# The responses of our API are G-zipped and you need to unpack them by using the proper response header encoding: Content-Encoding: gzip
# The date and time in the Search API are in the iso timestamp format.