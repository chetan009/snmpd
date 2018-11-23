# PySNMP SMI module. Autogenerated from smidump -f python IANA-MALLOC-MIB
# by libsmi2pysnmp-0.1.3 at Mon Apr  2 20:39:06 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class IANAmallocRangeSource(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,1,3,)
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3), )
    
class IANAscopeSource(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(5,1,4,3,2,)
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3), ("mzap", 4), ("madcap", 5), )
    

# Objects

ianaMallocMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 102)).setRevisions(("2003-01-27 12:00",))
if mibBuilder.loadTexts: ianaMallocMIB.setOrganization("IANA")
if mibBuilder.loadTexts: ianaMallocMIB.setContactInfo(" Internet Assigned Numbers Authority\nInternet Corporation for Assigned Names and Numbers\n4676 Admiralty Way, Suite 330\nMarina del Rey, CA 90292-6601\n\nPhone: +1 310 823 9358\nEMail: iana&iana.org")
if mibBuilder.loadTexts: ianaMallocMIB.setDescription("This MIB module defines the IANAscopeSource and\nIANAmallocRangeSource textual conventions for use in MIBs\nwhich need to identify ways of learning multicast scope and\nrange information.\n\nAny additions or changes to the contents of this MIB module\nrequire either publication of an RFC, or Designated Expert\nReview as defined in the Guidelines for Writing IANA\nConsiderations Section document.  The Designated Expert will\nbe selected by the IESG Area Director(s) of the Transport\nArea.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("IANA-MALLOC-MIB", PYSNMP_MODULE_ID=ianaMallocMIB)

# Types
mibBuilder.exportSymbols("IANA-MALLOC-MIB", IANAmallocRangeSource=IANAmallocRangeSource, IANAscopeSource=IANAscopeSource)

# Objects
mibBuilder.exportSymbols("IANA-MALLOC-MIB", ianaMallocMIB=ianaMallocMIB)
