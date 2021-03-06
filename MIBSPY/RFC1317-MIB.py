# PySNMP SMI module. Autogenerated from smidump -f python RFC1317-MIB
# by libsmi2pysnmp-0.1.3 at Thu Sep  6 11:51:08 2018,
# Python version sys.version_info(major=2, minor=7, micro=12, releaselevel='final', serial=0)

# Imports

( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Objects

rs232 = MibIdentifier((0, 33))
rs232Number = MibScalar((0, 33, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232Number.setDescription("The number of ports (regardless of their current\nstate) in the RS-232-like general port table.")
rs232PortTable = MibTable((0, 33, 2))
if mibBuilder.loadTexts: rs232PortTable.setDescription("A list of port entries.  The number of entries is\ngiven by the value of rs232Number.")
rs232PortEntry = MibTableRow((0, 33, 2, 1)).setIndexNames((0, "RFC1317-MIB", "rs232PortIndex"))
if mibBuilder.loadTexts: rs232PortEntry.setDescription("Status and parameter values for a port.")
rs232PortIndex = MibTableColumn((0, 33, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortIndex.setDescription("A unique value for each port.  Its value ranges\nbetween 1 and the value of rs232Number.  By\nconvention and if possible, hardware port numbers\nmap directly to external connectors.  The value for\neach port must remain constant at least from one\nre-initialization of the network management agent to\nthe next.")
rs232PortType = MibTableColumn((0, 33, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(5,1,2,3,4,)).subtype(namedValues=NamedValues(("other", 1), ("rs232", 2), ("rs422", 3), ("rs423", 4), ("v35", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortType.setDescription("The port's hardware type.")
rs232PortInSigNumber = MibTableColumn((0, 33, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortInSigNumber.setDescription("The number of input signals for the port in the\ninput signal table (rs232PortInSigTable).  The table\ncontains entries only for those signals the software\ncan detect.")
rs232PortOutSigNumber = MibTableColumn((0, 33, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortOutSigNumber.setDescription("The number of output signals for the port in the\noutput signal table (rs232PortOutSigTable).  The\ntable contains entries only for those signals the\nsoftware can assert.")
rs232PortInSpeed = MibTableColumn((0, 33, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortInSpeed.setDescription("The port's input speed in bits per second.")
rs232PortOutSpeed = MibTableColumn((0, 33, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortOutSpeed.setDescription("The port's output speed in bits per second.")
rs232AsyncPortTable = MibTable((0, 33, 3))
if mibBuilder.loadTexts: rs232AsyncPortTable.setDescription("A list of asynchronous port entries.  The maximum\nentry number is given by the value of rs232Number.\n\nEntries need not exist for synchronous ports.")
rs232AsyncPortEntry = MibTableRow((0, 33, 3, 1)).setIndexNames((0, "RFC1317-MIB", "rs232AsyncPortIndex"))
if mibBuilder.loadTexts: rs232AsyncPortEntry.setDescription("Status and parameter values for an asynchronous\nport.")
rs232AsyncPortIndex = MibTableColumn((0, 33, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortIndex.setDescription("A unique value for each port.  Its value is the\nsame as rs232PortIndex for the port.")
rs232AsyncPortBits = MibTableColumn((0, 33, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortBits.setDescription("The port's number of bits in a character.")
rs232AsyncPortStopBits = MibTableColumn((0, 33, 3, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,4,2,3,)).subtype(namedValues=NamedValues(("one", 1), ("two", 2), ("one-and-half", 3), ("dynamic", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortStopBits.setDescription("The port's number of stop bits.")
rs232AsyncPortParity = MibTableColumn((0, 33, 3, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,5,4,2,)).subtype(namedValues=NamedValues(("none", 1), ("odd", 2), ("even", 3), ("mark", 4), ("space", 5), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortParity.setDescription("The port's sense of a character parity bit.")
rs232AsyncPortAutobaud = MibTableColumn((0, 33, 3, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortAutobaud.setDescription("A control for the port's ability to automatically\nsense input speed.\n\nWhen rs232PortAutoBaud is 'enabled', a port may\nautobaud to values different from the set values for\nspeed, parity, and character size.  As a result a\nnetwork management system may temporarily observe\nvalues different from what was previously set.")
rs232SyncPortTable = MibTable((0, 33, 4))
if mibBuilder.loadTexts: rs232SyncPortTable.setDescription("A list of synchronous port entries.  The maximum\nentry number is given by the value of rs232Number.\nEntries need not exist for asynchronous ports.")
rs232SyncPortEntry = MibTableRow((0, 33, 4, 1)).setIndexNames((0, "RFC1317-MIB", "rs232SyncPortIndex"))
if mibBuilder.loadTexts: rs232SyncPortEntry.setDescription("Status and parameter values for a synchronous\nport.")
rs232SyncPortIndex = MibTableColumn((0, 33, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortIndex.setDescription("A unique value for each port.  Its value is the\nsame as rs232PortIndex for the port.")
rs232SyncPortClockSource = MibTableColumn((0, 33, 4, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,)).subtype(namedValues=NamedValues(("internal", 1), ("external", 2), ("split", 3), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortClockSource.setDescription("Source of the port's bit rate clock. 'split' means\nthe tranmit clock is internal and the receive clock\nis external.")
rs232InSigTable = MibTable((0, 33, 5))
if mibBuilder.loadTexts: rs232InSigTable.setDescription("A list of port input control signal entries.")
rs232InSigEntry = MibTableRow((0, 33, 5, 1)).setIndexNames((0, "RFC1317-MIB", "rs232InSigPortIndex"), (0, "RFC1317-MIB", "rs232InSigName"))
if mibBuilder.loadTexts: rs232InSigEntry.setDescription("Input control signal status for a hardware port.")
rs232InSigPortIndex = MibTableColumn((0, 33, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigPortIndex.setDescription("The value of rs232PortIndex for the port to which\nthis entry belongs.")
rs232InSigName = MibTableColumn((0, 33, 5, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(6,1,4,11,2,9,7,3,8,10,5,)).subtype(namedValues=NamedValues(("rts", 1), ("scts", 10), ("sdcd", 11), ("cts", 2), ("dsr", 3), ("dtr", 4), ("ri", 5), ("dcd", 6), ("sq", 7), ("srs", 8), ("srts", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigName.setDescription("Identification of a hardware signal, as follows:\n\nrts    Request to Send\ncts    Clear to Send\ndsr    Data Set Ready\ndtr    Data Terminal Ready\n\nri     Ring Indicator\ndcd    Received Line Signal Detector\nsq     Signal Quality Detector\nsrs    Data Signaling Rate Selector\nsrts   Secondary Request to Send\nscts   Secondary Clear to Send\nsdcd   Secondary Received Line Signal Detector")
rs232InSigState = MibTableColumn((0, 33, 5, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigState.setDescription("The current signal state.")
rs232OutSigTable = MibTable((0, 33, 6))
if mibBuilder.loadTexts: rs232OutSigTable.setDescription("A list of port output control signal entries.")
rs232OutSigEntry = MibTableRow((0, 33, 6, 1)).setIndexNames((0, "RFC1317-MIB", "rs232OutSigPortIndex"), (0, "RFC1317-MIB", "rs232OutSigName"))
if mibBuilder.loadTexts: rs232OutSigEntry.setDescription("Output control signal status for a hardware port.")
rs232OutSigPortIndex = MibTableColumn((0, 33, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigPortIndex.setDescription("The value of rs232PortIndex for the port to which\nthis entry belongs.")
rs232OutSigName = MibTableColumn((0, 33, 6, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(6,1,4,11,2,9,7,3,8,10,5,)).subtype(namedValues=NamedValues(("rts", 1), ("scts", 10), ("sdcd", 11), ("cts", 2), ("dsr", 3), ("dtr", 4), ("ri", 5), ("dcd", 6), ("sq", 7), ("srs", 8), ("srts", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigName.setDescription("Identification of a hardware signal, as follows:\n\nrts    Request to Send\ncts    Clear to Send\ndsr    Data Set Ready\ndtr    Data Terminal Ready\nri     Ring Indicator\ndcd    Received Line Signal Detector\nsq     Signal Quality Detector\nsrs    Data Signaling Rate Selector\nsrts   Secondary Request to Send\nscts   Secondary Clear to Send\nsdcd   Secondary Received Line Signal Detector")
rs232OutSigState = MibTableColumn((0, 33, 6, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigState.setDescription("The current signal state.")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("RFC1317-MIB", rs232=rs232, rs232Number=rs232Number, rs232PortTable=rs232PortTable, rs232PortEntry=rs232PortEntry, rs232PortIndex=rs232PortIndex, rs232PortType=rs232PortType, rs232PortInSigNumber=rs232PortInSigNumber, rs232PortOutSigNumber=rs232PortOutSigNumber, rs232PortInSpeed=rs232PortInSpeed, rs232PortOutSpeed=rs232PortOutSpeed, rs232AsyncPortTable=rs232AsyncPortTable, rs232AsyncPortEntry=rs232AsyncPortEntry, rs232AsyncPortIndex=rs232AsyncPortIndex, rs232AsyncPortBits=rs232AsyncPortBits, rs232AsyncPortStopBits=rs232AsyncPortStopBits, rs232AsyncPortParity=rs232AsyncPortParity, rs232AsyncPortAutobaud=rs232AsyncPortAutobaud, rs232SyncPortTable=rs232SyncPortTable, rs232SyncPortEntry=rs232SyncPortEntry, rs232SyncPortIndex=rs232SyncPortIndex, rs232SyncPortClockSource=rs232SyncPortClockSource, rs232InSigTable=rs232InSigTable, rs232InSigEntry=rs232InSigEntry, rs232InSigPortIndex=rs232InSigPortIndex, rs232InSigName=rs232InSigName, rs232InSigState=rs232InSigState, rs232OutSigTable=rs232OutSigTable, rs232OutSigEntry=rs232OutSigEntry, rs232OutSigPortIndex=rs232OutSigPortIndex, rs232OutSigName=rs232OutSigName, rs232OutSigState=rs232OutSigState)

