#include <pcap.h>
#include <stdio.h>
#include <arpa/inet.h>


struct ethheader {
	u_char ether_dhost[6];
	u_char ether_shost[6];
	u_short ether_type;
};
struct ipheader {
	unsigned char iph_ihl:4, iph_ver:4;
	unsigned char iph_tos;
	unsigned short int iph_len;
	unsigned short int iph_ident;
	unsigned short int iph_flag:3, iph_offset:13;
	unsigned char iph_ttl;
	unsigned char iph_protocol;
	unsigned short int iph_chksum;
	struct in_addr iph_sourceip;
	struct in_addr iph_destip;
};


void got_packet(u_char *args, const struct pcap_pkthdr *header,const u_char *packet)
{	
	struct ethheader *eth = (struct ethheader *)packet;
	if (ntohs(eth->ether_type) == 0x0800){
		struct ipheader * ip = (struct ipheader *)(packet + sizeof(struct ethheader));
		printf("   From : %s\n", inet_ntoa(ip->iph_sourceip) );
		 printf("   To : %s\n", inet_ntoa(ip->iph_destip) );
	}
}
int main(){
pcap_t *handle;
char errbuf[PCAP_ERRBUF_SIZE];
struct bpf_program fp;
char filter_exp[] = "ip proto icmp";
bpf_u_int32 net;
// Step 1: Open live pcap session on NIC with name enp0s3
handle = pcap_open_live("enp0s3", BUFSIZ, 1, 1000, errbuf);
// Step 2: Compile filter_exp into BPF psuedo-code
pcap_compile(handle, &fp, filter_exp, 0, net);
pcap_setfilter(handle, &fp);
// Step 3: Capture packets
pcap_loop(handle, -1, got_packet, NULL);
pcap_close(handle); //Close the handle
return 0;
}


