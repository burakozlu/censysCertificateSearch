from censys.search import CensysCertificates

def certSearch(filename):
    c = CensysCertificates("API ID","Secret")

    file = open("foundcerts.txt","a")
    dfile = open(f"{filename}","r")
    
    for domain in dfile:
        for page in c.search(f'"{domain}" AND parsed.issuer.organization.raw: "Let\'s Encrypt" OR parsed.issuer.organization.raw: "COMODO CA Limited"',max_records=1000):
            r = page["parsed.fingerprint_sha256"] + " | " +page["parsed.subject_dn"] + "\n"
            file.write(r)
            print(r)
    
    file.close()
    dfile.close()


certSearch(input("enter filename that contains domains : "))