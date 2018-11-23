# PySNMP SMI module. Autogenerated from smidump -f python TN3270E-RT-MIB
# by libsmi2pysnmp-0.1.3 at Mon Apr  2 20:39:45 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( IANATn3270eAddrType, IANATn3270eAddress, ) = mibBuilder.importSymbols("IANATn3270eTC-MIB", "IANATn3270eAddrType", "IANATn3270eAddress")
( snanauMIB, ) = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DateAndTime, RowStatus, TestAndIncr, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TestAndIncr", "TimeStamp")
( tn3270eClientGroupName, tn3270eResMapElementType, tn3270eSrvrConfIndex, ) = mibBuilder.importSymbols("TN3270E-MIB", "tn3270eClientGroupName", "tn3270eResMapElementType", "tn3270eSrvrConfIndex")

# Objects

tn3270eRtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 9)).setRevisions(("1998-07-27 00:00",))
if mibBuilder.loadTexts: tn3270eRtMIB.setOrganization("TN3270E Working Group")
if mibBuilder.loadTexts: tn3270eRtMIB.setContactInfo("Kenneth White (kennethw@vnet.ibm.com)\nIBM Corp. - Dept. BRQA/Bldg. 501/G114\nP.O. Box 12195\n3039 Cornwallis\nRTP, NC 27709-2195\n\nRobert Moore (remoore@us.ibm.com)\nIBM Corp. - Dept. BRQA/Bldg. 501/G114\nP.O. Box 12195\n3039 Cornwallis\nRTP, NC 27709-2195\n(919) 254-4436")
if mibBuilder.loadTexts: tn3270eRtMIB.setDescription("This module defines a portion of the management\ninformation base (MIB) that enables monitoring of\nTN3270 and TN3270E clients' response times by a\nTN3270E server.")
tn3270eRtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 0))
tn3270eRtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 1))
tn3270eRtCollCtlTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 1))
if mibBuilder.loadTexts: tn3270eRtCollCtlTable.setDescription("The response time monitoring collection control table,\nwhich allows a management application to control the\ntypes of response time data being collected, and the\nclients for which it is being collected.\n\nThis table is indexed by tn3270eSrvrConfIndex and\ntn3270eClientGroupName imported from the\nTN3270E-MIB.  tn3270eSrvrConfIndex indicates within\na host which TN3270E server an entry applies to.\ntn3270eClientGroupName it identifies the set of IP\nclients for which response time data is being collected.\nThe particular IP clients making up the set are identified\nin the tn3270eClientGroupTable in the TN3270E-MIB.")
tn3270eRtCollCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"))
if mibBuilder.loadTexts: tn3270eRtCollCtlEntry.setDescription("An entry in the TN3270E response time monitoring collection\ncontrol table.  To handle the case of multiple TN3270E\nservers on the same host, the first index of this table is\nthe tn3270eSrvrConfIndex from the TN3270E-MIB.")
tn3270eRtCollCtlType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 2), Bits().subtype(namedValues=NamedValues(("aggregate", 0), ("excludeIpComponent", 1), ("ddr", 2), ("average", 3), ("buckets", 4), ("traps", 5), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlType.setDescription("This object controls what types of response time data to\ncollect, whether to summarize the data across the members\nof a client group or keep it individually, whether to\nintroduce dynamic definite responses, and whether to\ngenerate traps.\naggregate(0)          - Aggregate response time data for the\n                        client group as a whole.  If this bit\n                        is set to 0, then maintain response\n                        time data separately for each member\n                        of the client group.\nexcludeIpComponent(1) - Do not include the IP-network\n                        component in any response times.\nddr(2)                - Enable dynamic definite response.\naverage(3)            - Produce an average response time\n                        based on a specified collection\n                        interval.\nbuckets(4)            - Maintain tn3270eRtDataBucket values in\n                        a corresponding tn3270eRtDataEntry,\n                        based on the bucket boundaries specified\n                        in the tn3270eRtCollCtlBucketBndry\n                        objects          .\ntraps(5)              - generate the notifications specified\n                        in this MIB module.  The\n                        tn3270eRtExceeded and tn3270eRtOkay\n                        notifications are generated only if\n                        average(3) is also specified.")
tn3270eRtCollCtlSPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 86400)).clone(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPeriod.setDescription("The number of seconds that defines the sample period.\nThe actual interval is defined as tn3270eRtCollCtlSPeriod\ntimes tn3270eRtCollCtlSPMult.\n\nThe value of this object is used only if the corresponding\ntn3270eRtCollCtlType has the average(3) setting.")
tn3270eRtCollCtlSPMult = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 5760)).clone(30)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPMult.setDescription("The sample period multiplier; this value is multiplied by\nthe sample period, tn3270eRtCollCtlSPeriod, to determine\nthe collection interval.\nSliding-window average calculation can, if necessary, be\ndisabled, by setting the sample period multiplier,\ntn3270eRtCollCtlSPMult, to 1, and setting the sample\nperiod, tn3270eRtCollCtlSPeriod, to the required\ncollection interval.\n\nThe value of this object is used only if the corresponding\ntn3270eRtCollCtlType has the average(3) setting.")
tn3270eRtCollCtlThreshHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 5), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshHigh.setDescription("The threshold for generating a tn3270eRtExceeded\nnotification, signalling that a monitored total response\ntime has exceeded the specified limit.  A value of zero\nfor this object suppresses generation of this notification.\nThe value of this object is used only if the corresponding\ntn3270eRtCollCtlType has average(3) and traps(5) selected.\n\nA tn3270eRtExceeded notification is not generated again for a\ntn3270eRtDataEntry until an average response time falling below\nthe low threshold tn3270eRtCollCtlThreshLow specified for the\nclient group has occurred for the entry.")
tn3270eRtCollCtlThreshLow = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 6), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshLow.setDescription("The threshold for generating a tn3270eRtOkay notification,\nsignalling that a monitored total response time has fallen\nbelow the specified limit.  A value of zero for this object\nsuppresses generation of this notification.  The value of\nthis object is used only if the corresponding\ntn3270eRtCollCtlType has average(3) and traps(5) selected.\n\nA tn3270eRtOkay notification is not generated again for a\ntn3270eRtDataEntry until an average response time\nexceeding the high threshold tn3270eRtCollCtlThreshHigh\nspecified for the client group has occurred for the entry.")
tn3270eRtCollCtlIdleCount = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 7), Unsigned32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlIdleCount.setDescription("The value of this object is used to determine whether a\nsample that yields an average response time exceeding the\nvalue of tn3270eRtCollCtlThreshHigh was a statistically\nvalid one.  If the following statement is true, then the\nsample was statistically valid, and so a tn3270eRtExceeded\nnotification should be generated:\n\n  AvgCountTrans * ((AvgRt/ThreshHigh - 1) ** 2) >=  IdleCount\n\nThis comparison is done only if the corresponding\ntn3270eRtCollCtlType has average(3) and traps(5) selected.")
tn3270eRtCollCtlBucketBndry1 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 8), Unsigned32().clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry1.setDescription("The value of this object defines the range of transaction\nresponse times counted in the Tn3270eRtDataBucket1Rts\nobject: those less than or equal to this value.")
tn3270eRtCollCtlBucketBndry2 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 9), Unsigned32().clone(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry2.setDescription("The value of this object, together with that of the\ntn3270eRtCollCtlBucketBndry1 object, defines the range\nof transaction response times counted in the\nTn3270eRtDataBucket2Rts object: those greater than the\nvalue of the tn3270eRtCollCtlBucketBndry1 object, and\nless than or equal to the value of this object.")
tn3270eRtCollCtlBucketBndry3 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 10), Unsigned32().clone(50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry3.setDescription("The value of this object, together with that of the\ntn3270eRtCollCtlBucketBndry2 object, defines the range of\ntransaction response times counted in the\nTn3270eRtDataBucket3Rts object:  those greater than the\nvalue of the tn3270eRtCollCtlBucketBndry2 object, and less\nthan or equal to the value of this object.")
tn3270eRtCollCtlBucketBndry4 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 11), Unsigned32().clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry4.setDescription("The value of this object, together with that of the\ntn3270eRtCollCtlBucketBndry3 object, defines the range\nof transaction response times counted in the\nTn3270eRtDataBucket4Rts object: those greater than the\nvalue of the tn3270eRtCollCtlBucketBndry3 object, and\nless than or equal to the value of this object.\n\nThe value of this object also defines the range of\ntransaction response times counted in the\nTn3270eRtDataBucket5Rts object: those greater than the\nvalue of this object.")
tn3270eRtCollCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlRowStatus.setDescription("This object allows entries to be created and deleted\nin the tn3270eRtCollCtlTable.  An entry in this table\nis deleted by setting this object to destroy(6).\nDeleting an entry in this table has the side-effect\nof removing all entries from the tn3270eRtDataTable\nthat are associated with the entry being deleted.")
tn3270eRtDataTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 2))
if mibBuilder.loadTexts: tn3270eRtDataTable.setDescription("The response time data table.  Entries in this table are\ncreated based on entries in the tn3270eRtCollCtlTable.")
tn3270eRtDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddrType"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddress"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientPort"))
if mibBuilder.loadTexts: tn3270eRtDataEntry.setDescription("Entries in this table are created based upon the\ntn3270eRtCollCtlTable.  When the corresponding\ntn3270eRtCollCtlType has aggregate(0) specified, a single\nentry is created in this table, with a tn3270eRtDataClientAddrType\nof unknown(0), a zero-length octet string value for\ntn3270eRtDataClientAddress, and a tn3270eRtDataClientPort value of\n0.  When aggregate(0) is not specified, a separate entry is\ncreated for each client in the group.\n\nNote that the following objects defined within an entry in this\ntable can  wrap:\n    tn3270eRtDataTotalRts\n    tn3270eRtDataTotalIpRts\n    tn3270eRtDataCountTrans\n    tn3270eRtDataCountDrs\n    tn3270eRtDataElapsRnTrpSq\n    tn3270eRtDataElapsIpRtSq\n    tn3270eRtDataBucket1Rts\n    tn3270eRtDataBucket2Rts\n    tn3270eRtDataBucket3Rts\n    tn3270eRtDataBucket4Rts\n    tn3270eRtDataBucket5Rts")
tn3270eRtDataClientAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 1), IANATn3270eAddrType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tn3270eRtDataClientAddrType.setDescription("Indicates the type of address represented by the value\nof tn3270eRtDataClientAddress.  The value unknown(0) is\nused if aggregate data is being collected for the client\ngroup.")
tn3270eRtDataClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 2), IANATn3270eAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tn3270eRtDataClientAddress.setDescription("Contains the IP address of the TN3270 client being\nmonitored.  A zero-length octet string is used if\naggregate data is being collected for the client group.")
tn3270eRtDataClientPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tn3270eRtDataClientPort.setDescription("Contains the client port number of the TN3270 client being\nmonitored.  The value 0 is used if aggregate data is being\ncollected for the client group, or if the\ntn3270eRtDataClientAddrType identifies an address type that\ndoes not support ports.")
tn3270eRtDataAvgRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 4), Gauge32().clone('0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgRt.setDescription("The average total response time measured over the last\ncollection interval.")
tn3270eRtDataAvgIpRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 5), Gauge32().clone('0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgIpRt.setDescription("The average IP response time measured over the last\ncollection interval.")
tn3270eRtDataAvgCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgCountTrans.setDescription("The sliding transaction count used for calculating the\nvalues of the tn3270eRtDataAvgRt and tn3270eRtDataAvgIpRt\nobjects.  The actual transaction count is available in\nthe tn3270eRtDataCountTrans object.\n\nThe initial value of this object, before any averages have\nbeen calculated, is 0.")
tn3270eRtDataIntTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataIntTimeStamp.setDescription("The date and time of the last interval that\ntn3270eRtDataAvgRt, tn3270eRtDataAvgIpRt, and\ntn3270eRtDataAvgCountTrans were calculated.\n\nPrior to the calculation of the first interval\naverages, this object returns the value\n0x0000000000000000000000.  When this value is\nreturned, the remaining objects in the entry have\nno significance.")
tn3270eRtDataTotalRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalRts.setDescription("The count of the total response times collected.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataTotalIpRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalIpRts.setDescription("The count of the total IP-network response times\ncollected.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountTrans.setDescription("The count of the total number of transactions detected.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataCountDrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountDrs.setDescription("The count of the total number of definite responses\ndetected.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataElapsRndTrpSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 12), Unsigned32().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsRndTrpSq.setDescription("The sum of the elapsed round trip time squared.  The sum\nof the squares is kept in order to enable calculation of\na variance.")
tn3270eRtDataElapsIpRtSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 13), Unsigned32().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsIpRtSq.setDescription("The sum of the elapsed IP round trip time squared.\nThe sum of the squares is kept in order to enable\ncalculation of a variance.")
tn3270eRtDataBucket1Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket1Rts.setDescription("The count of the response times falling into bucket 1.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataBucket2Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket2Rts.setDescription("The count of the response times falling into bucket 2.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataBucket3Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket3Rts.setDescription("The count of the response times falling into bucket 3.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataBucket4Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket4Rts.setDescription("The count of the response times falling into bucket 4.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataBucket5Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket5Rts.setDescription("The count of the response times falling into bucket 5.\n\nA management application can detect discontinuities in this\ncounter by monitoring the tn3270eRtDataDiscontinuityTime\nobject.")
tn3270eRtDataRtMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 19), Integer().subtype(subtypeSpec=SingleValueConstraint(0,2,1,)).subtype(namedValues=NamedValues(("none", 0), ("responses", 1), ("timingMark", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataRtMethod.setDescription("The value of this object indicates the method that was\nused in calculating the IP network time.\n\nThe value 'none(0) indicates that response times were not\ncalculated for the IP network.")
tn3270eRtDataDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 20), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at\nwhich one or more of this entry's counter objects\nsuffered a discontinuity.  This may happen if a TN3270E\nserver is stopped and then restarted, and local methods\nare used to set up collection policy\n(tn3270eRtCollCtlTable entries).")
tn3270eRtSpinLock = MibScalar((1, 3, 6, 1, 2, 1, 34, 9, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tn3270eRtSpinLock.setDescription("An advisory lock used to allow cooperating TN3270E-RT-MIB\napplications to coordinate their use of the\ntn3270eRtCollCtlTable.\nWhen creating a new entry or altering an existing entry\nin the tn3270eRtCollCtlTable, an application should make\nuse of tn3270eRtSpinLock to serialize application changes\nor additions.\n\nSince this is an advisory lock, the use of this lock is\nnot enforced.")
tn3270eRtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3))
tn3270eRtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 1))
tn3270eRtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 2))

# Augmentions

# Notifications

tn3270eRtExceeded = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 1)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ) )
if mibBuilder.loadTexts: tn3270eRtExceeded.setDescription("This notification is generated when the average response\ntime, tn3270eRtDataAvgRt, exceeds\ntn3270eRtCollCtlThresholdHigh at the end of a collection\ninterval specified by tn3270eCollCtlSPeriod\ntimes tn3270eCollCtlSPMult.  Note that the corresponding\ntn3270eCollCtlType must have traps(5) and average(3) set\nfor this notification to be generated.  In addition,\ntn3270eRtDataAvgCountTrans, tn3270eRtCollCtlThreshHigh, and\ntn3270eRtDataAvgRt are algorithmically compared to\ntn3270eRtCollCtlIdleCount for determination if this\nnotification will be suppressed.")
tn3270eRtOkay = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 2)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ) )
if mibBuilder.loadTexts: tn3270eRtOkay.setDescription("This notification is generated when the average response\ntime, tn3270eRtDataAvgRt, falls below\ntn3270eRtCollCtlThresholdLow at the end of a collection\ninterval specified by tn3270eCollCtlSPeriod times\ntn3270eCollCtlSPMult, after a tn3270eRtExceeded\nnotification was generated.  Note that the corresponding\ntn3270eCollCtlType must have traps(5) and average(3)\nset for this notification to be generated.")
tn3270eRtCollStart = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 3)).setObjects(*(("TN3270E-MIB", "tn3270eResMapElementType"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ) )
if mibBuilder.loadTexts: tn3270eRtCollStart.setDescription("This notification is generated when response time data\ncollection is enabled for a member of a client group.\nIn order for this notification to occur the corresponding\ntn3270eRtCollCtlType must have traps(5) selected.\n\ntn3270eResMapElementType contains a valid value only if\ntn3270eRtDataClientAddress contains a valid address\n(rather than a zero-length octet string).")
tn3270eRtCollEnd = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 4)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ) )
if mibBuilder.loadTexts: tn3270eRtCollEnd.setDescription("This notification is generated when an tn3270eRtDataEntry\nis deleted after being active (actual data collected), in\norder to enable a management application monitoring an\ntn3270eRtDataEntry to get the entry's final values.  Note\nthat the corresponding tn3270eCollCtlType must have traps(5)\nset for this notification to be generated.")

# Groups

tn3270eRtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 1)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlIdleCount"), ("TN3270E-RT-MIB", "tn3270eRtSpinLock"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPMult"), ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPeriod"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshLow"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry3"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry2"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry1"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry4"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlRowStatus"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshHigh"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlType"), ) )
if mibBuilder.loadTexts: tn3270eRtGroup.setDescription("This group is mandatory for all implementations that\nsupport the TN3270E-RT-MIB. ")
tn3270eRtNotGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 2)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtCollEnd"), ("TN3270E-RT-MIB", "tn3270eRtExceeded"), ("TN3270E-RT-MIB", "tn3270eRtOkay"), ("TN3270E-RT-MIB", "tn3270eRtCollStart"), ) )
if mibBuilder.loadTexts: tn3270eRtNotGroup.setDescription("The notifications that must be supported when the\nTN3270E-RT-MIB is implemented. ")

# Compliances

tn3270eRtCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 9, 3, 2, 1)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtNotGroup"), ("TN3270E-RT-MIB", "tn3270eRtGroup"), ) )
if mibBuilder.loadTexts: tn3270eRtCompliance.setDescription("The compliance statement for agents that support the\nTN327E-RT-MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("TN3270E-RT-MIB", PYSNMP_MODULE_ID=tn3270eRtMIB)

# Objects
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtMIB=tn3270eRtMIB, tn3270eRtNotifications=tn3270eRtNotifications, tn3270eRtObjects=tn3270eRtObjects, tn3270eRtCollCtlTable=tn3270eRtCollCtlTable, tn3270eRtCollCtlEntry=tn3270eRtCollCtlEntry, tn3270eRtCollCtlType=tn3270eRtCollCtlType, tn3270eRtCollCtlSPeriod=tn3270eRtCollCtlSPeriod, tn3270eRtCollCtlSPMult=tn3270eRtCollCtlSPMult, tn3270eRtCollCtlThreshHigh=tn3270eRtCollCtlThreshHigh, tn3270eRtCollCtlThreshLow=tn3270eRtCollCtlThreshLow, tn3270eRtCollCtlIdleCount=tn3270eRtCollCtlIdleCount, tn3270eRtCollCtlBucketBndry1=tn3270eRtCollCtlBucketBndry1, tn3270eRtCollCtlBucketBndry2=tn3270eRtCollCtlBucketBndry2, tn3270eRtCollCtlBucketBndry3=tn3270eRtCollCtlBucketBndry3, tn3270eRtCollCtlBucketBndry4=tn3270eRtCollCtlBucketBndry4, tn3270eRtCollCtlRowStatus=tn3270eRtCollCtlRowStatus, tn3270eRtDataTable=tn3270eRtDataTable, tn3270eRtDataEntry=tn3270eRtDataEntry, tn3270eRtDataClientAddrType=tn3270eRtDataClientAddrType, tn3270eRtDataClientAddress=tn3270eRtDataClientAddress, tn3270eRtDataClientPort=tn3270eRtDataClientPort, tn3270eRtDataAvgRt=tn3270eRtDataAvgRt, tn3270eRtDataAvgIpRt=tn3270eRtDataAvgIpRt, tn3270eRtDataAvgCountTrans=tn3270eRtDataAvgCountTrans, tn3270eRtDataIntTimeStamp=tn3270eRtDataIntTimeStamp, tn3270eRtDataTotalRts=tn3270eRtDataTotalRts, tn3270eRtDataTotalIpRts=tn3270eRtDataTotalIpRts, tn3270eRtDataCountTrans=tn3270eRtDataCountTrans, tn3270eRtDataCountDrs=tn3270eRtDataCountDrs, tn3270eRtDataElapsRndTrpSq=tn3270eRtDataElapsRndTrpSq, tn3270eRtDataElapsIpRtSq=tn3270eRtDataElapsIpRtSq, tn3270eRtDataBucket1Rts=tn3270eRtDataBucket1Rts, tn3270eRtDataBucket2Rts=tn3270eRtDataBucket2Rts, tn3270eRtDataBucket3Rts=tn3270eRtDataBucket3Rts, tn3270eRtDataBucket4Rts=tn3270eRtDataBucket4Rts, tn3270eRtDataBucket5Rts=tn3270eRtDataBucket5Rts, tn3270eRtDataRtMethod=tn3270eRtDataRtMethod, tn3270eRtDataDiscontinuityTime=tn3270eRtDataDiscontinuityTime, tn3270eRtSpinLock=tn3270eRtSpinLock, tn3270eRtConformance=tn3270eRtConformance, tn3270eRtGroups=tn3270eRtGroups, tn3270eRtCompliances=tn3270eRtCompliances)

# Notifications
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtExceeded=tn3270eRtExceeded, tn3270eRtOkay=tn3270eRtOkay, tn3270eRtCollStart=tn3270eRtCollStart, tn3270eRtCollEnd=tn3270eRtCollEnd)

# Groups
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtGroup=tn3270eRtGroup, tn3270eRtNotGroup=tn3270eRtNotGroup)

# Compliances
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtCompliance=tn3270eRtCompliance)