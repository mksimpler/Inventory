import mock_catalyst
from mock_catalyst import EndOfApplication
from main import main

from vocollect_lut_odr_test.mock_server import MockServer, BOTH_SERVERS
server = MockServer(True, 15008, 15009)
server.set_server_response('5 4 X 3 2,123\r\n\r\n', 'LUTLocation')
server.set_server_response('5 4 X 3 2,456\r\n5 4 X 3 2,12\r\n\r\n', 'LUTBackStock')
server.set_server_response('X', 'ODRCount')
server.start_server(BOTH_SERVERS)

mock_catalyst.environment_properties['SwVersion.Locale'] = 'en_US'

try:
    main()
except EndOfApplication:
    print('Application ended')
    
server.stop_server(BOTH_SERVERS)