import dns
import dns.resolver

dnsA = dns.resolver.resolve('google.com', 'A');
print('A')
for respuesta in dnsA:
    print(respuesta);
    
dnsAAAA = dns.resolver.resolve('google.com', 'AAAA');
for respuesta in dnsAAAA:
    print(respuesta);
    
dnsMx = dns.resolver.resolve('google.com', 'MX');
print('MX')
for respuesta in dnsMx:
    print(respuesta);
    
dnsNS = dns.resolver.resolve('google.com', 'NS');
print('NS')
for respuesta in dnsNS:
    print(respuesta);

name1= dns.name.from_text('www.google.com');
name2= dns.name.from_text('google.com');

print(name1);
print(name2);