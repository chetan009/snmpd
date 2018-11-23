# PySNMP SMI module. Autogenerated from smidump -f python TRIP-TC-MIB
# by libsmi2pysnmp-0.1.3 at Mon Apr  2 20:39:47 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class TripAddressFamily(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,255,3,2,)
    namedValues = NamedValues(("decimal", 1), ("pentadecimal", 2), ("other", 255), ("e164", 3), )
    
class TripAppProtocol(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,1,3,4,255,)
    namedValues = NamedValues(("sip", 1), ("q931", 2), ("other", 255), ("ras", 3), ("annexG", 4), )
    
class TripCommunityId(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)
    
class TripId(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)
    
class TripItad(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)
    
class TripProtocolVersion(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,255)
    
class TripSendReceiveMode(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,1,3,)
    namedValues = NamedValues(("sendReceive", 1), ("sendOnly", 2), ("receiveOnly", 3), )
    

# Objects

tripTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 115)).setRevisions(("2004-09-02 00:00",))
if mibBuilder.loadTexts: tripTC.setOrganization("IETF IPTel Working Group.\nMailing list: iptel@lists.bell-labs.com")
if mibBuilder.loadTexts: tripTC.setContactInfo("Co-editor  David Zinman\npostal:    265 Ridley Blvd.\n           Toronto ON, M5M 4N8\n           Canada\nemail:     dzinman@rogers.com\nphone:     +1 416 433 4298\n\nCo-editor: David Walker\n           Sedna Wireless Inc.\npostal:    495 March Road, Suite 500\n           Ottawa, ON K2K 3G1\n           Canada\nemail:     david.walker@sedna-wireless.com\nphone:     +1 613 878 8142\n\nCo-editor   Jianping Jiang\n            Syndesis Limited\npostal:     30 Fulton Way\n            Richmond Hill, ON L4B 1J5\n            Canada\n\nemail:      jjiang@syndesis.com\nphone:      +1 905 886-7818 x2515")
if mibBuilder.loadTexts: tripTC.setDescription("Initial version of TRIP (Telephony Routing Over IP)\nMIB Textual Conventions module used by other\n\n\n\nTRIP-related MIB Modules.\n\nCopyright (C) The Internet Society (2004). This version of\nthis MIB module is part of RFC 3872, see the RFC itself\nfor full legal notices.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("TRIP-TC-MIB", PYSNMP_MODULE_ID=tripTC)

# Types
mibBuilder.exportSymbols("TRIP-TC-MIB", TripAddressFamily=TripAddressFamily, TripAppProtocol=TripAppProtocol, TripCommunityId=TripCommunityId, TripId=TripId, TripItad=TripItad, TripProtocolVersion=TripProtocolVersion, TripSendReceiveMode=TripSendReceiveMode)

# Objects
mibBuilder.exportSymbols("TRIP-TC-MIB", tripTC=tripTC)
