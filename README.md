stuff




* 2071  python csv_ip_host.py host2ip subdomains.csv 
* 2072  python csv_ip_host.py host2ip subdomains.csv t
* 2073  cat ttest.csv
* 2074  awk -F "\"*,\"*" '{print $2}' ttest.csv
* 2075  awk -F "\"*,\"*" '{print $2}' ttest.csv | sed 's/,$//'
* 2076  awk -F "\"*,\"*" '{print $2}' ttest.csv > ipstest
* 2077  sed 's/.$//' ipstest
* 2078  awk '{gsub(/,$/,""); print}' ipstest
* 2079  cat ipstest
* 2080  cat ipstest | sed 's/"//g'
* 2081  awk -F "\"*,\"*" '{print $2}' ttest.csv  | sed 's/"//g'
* 2082  awk -F "\"*,\"*" '{print $1}' ttest.csv  | sed 's/"//g'
* 2083  cat ttest.csv
* 2084  cat ipstest | sed 's/"//g' > ipstest
* 2085  cat ipstest
* 2086  cat ipstest | xargs -L1 shodan host
* 2087  shodan host 198.245.94.222
* 2088  ls
* 2089  rm subdomains.csv
* 2090  rm ttest.csv
* 2091  rm ipstest
* 2094  ls
* 2095  cat ttest.csv
* 2096  awk -F "\"*,\"*" '{print $1}' ttest.csv  | sed 's/"//g'
* 2097  history
* 2098  awk -F "\"*,\"*" '{print $1}' ttest.csv  | sed 's/"//g'
* 2099  awk -F "\"*,\"*" '{print $2}' ttest.csv  | sed 's/"//g'
* 2100  awk -F "\"*,\"*" '{print $2}' ttest.csv  | sed 's/"//g' | xargs -L1 shodan host\n
* 2101  vim networks.txt
* 2102  cat etworks.txt | grep -E ^@(([a-zA-Z](-?[a-zA-Z0-9])*)\.)+[a-zA-Z]{2,}$\n
* 2103  cat works.txt | grep -E (([a-zA-Z](-?[a-zA-Z0-9])*)\.)+[a-zA-Z]{2,}$\n
* 2104  grep -P "^.[^.]+\.[a-zA-Z]{3}$|^.[^.]+\.[a-zA-Z]{2}\.[a-zA-Z]{2}$" s.txt
* 2105  grep *.com
* 2107  cat etworks.txt| grep *.com
* 2110  ls
* 2112  vim ips.txt
* 2113  python csv_ip_host.py host2ip ips.txt 1
* 2114  cat ttest.csv
* 2115  history 
* 2116  awk -F "\"*,\"*" '{print $2}' ttest.csv  | sed 's/"//g'\n
* 2117  awk -F "\"*,\"*" '{print $2}' ttest.csv  | sed 's/"//g' | xargs -L1 shodan host\n
* 2125  cat ips.txt | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}"
* 2126  cat ips.txt | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" | xargs -L1 shodan host\n
*
