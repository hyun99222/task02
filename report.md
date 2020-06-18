
# Task 02 (Packet Sniffing and Spoofing) Task Report Submission

## Author
 - **Student ID**: 2018270130
 - **Name**: Jihyun Lee
 - **GitHub ID**: hyun9922

## Task 1.1: Sniffing Packets

Task 1.1A(output.txt)과 Task 1.1B(output2.txt)을 수행했으며, 수행 내역은 Terminal Dump에 있습니다. 

## Task 1.2: Spoofing ICMP Packets
Task 1.2에서 Task Description에 따라 샘플 코드를 다음과 같이 수정했습니다. 수정한 파일의 이름은 `task1.2.py` 입니다.
수행내역은 task1.2.txt에 있으며 코드를 실행하면 스푸핑된 ICMP에코 요청이 생성되었습니다.(task1.2.txt,task1.2.py)
 
## Task 1.3: Traceroute
 Task Description에 따라 샘플 코드를 수정하여 실행했습니다. Wireshark를 이용하여 주고받은 패킷을 확인 할 수 있었습니다.(task1.3.txt)

## Task 1.4: Sniffing and-then Spoofing
-  두개의 VM을 만들었고 ICMP 패킷을 스니핑하고 ICMP 에코 회신이 생성되어 전송되었습니다. (task1.4.txt)

## Task 2.1: Writing Packet Sniffing Program
 - Task 2.1A는 <https://github.com/kevin-w-du/BookCode/tree/master/Sniffing_Spoofing>에 공개된 코드를 이용해 실험을 했으며, 
   수행내역은 Terminal Dump에 있습니다.(task2.c, task2.1.txt)

  **Question 1**. Please use your own words to describe the sequence of the library calls that are essential
for sniffer programs. This is meant to be a summary, not detailed explanation like the one in the
tutorial or book.
 - Answer: pcap세션을 열고 나서 pcap_compile()으로 필터를 컴파일하고 ,pcap_setfilter()으로 컴파일된 필터가 적용 후 
 pcap_close()를 사용하여 pcap 세션을 닫아야 합니다.

  **Question 2**. Why do you need the root privilege to run a sniffer program? Where does the program
fail if it is executed without the root privilege?

 - Answer: 스니퍼 프로그램을 실행할 때 루트 권한이 없으면 실행 프로그램에 오류가 발생하는데, 프로그램이 엑세스하는 동안 발생하는 것 입니다.
           스니퍼 프로그램은 네트워크 인터페이스 카드에 접속해야하기 때문에 루트 권한이 필요합니다.
 

  **Question 3**. Please turn on and turn off the promiscuous mode in your sniffer program. Can you
demonstrate the difference when this mode is on and off? Please describe how you can demonstrate
this.
(못함)
 - Answer: Promiscuous Mode를 꺼보고 실행하였더니 잘 작동 하였으나 Promiscuous Mode를 키고 하면 처리되지 않았다.


- Task 2.2B에 주어진 상황에 따라 filter expression을 만들어 실험했으며, 수행 내역은 Terminal Dump에 있습니다. filter expression은 다음과 같습니다.
  (task2.2b.c)
    - 1.icmp and src host 10.0.2.6 and dst host 8.8.8.8로 바꿔서 하였습니다.(task2b.txt)
    - 2.tcp and dst portange 10-100(task2b-2.txt)
    

 - Task 2.1C 상황에 따라 telnet 접속을 시도해서 패스워드가 검색되는 걸 확인하였 (or 검색이 안 되었)습니다.
 

## Task 2.2:Spoofing

- Task 2.2A:Write a spoofing program

- Task 2.2B:Spoof an ICMP Echo Request

* **Question 4**. Can you set the IP packet length ﬁeld to an arbitrary value, regardless of how big the actual packet is? 

* **Question 5**. Using the raw socket programming, do you have to calculate the checksum for the IP header? 
 계산할 필요 없습니다. 패킷이 전송되면 시스템이 해당 필드를 채우기 때문에 IP 헤더의 체크섬 필드를 채울 필요가 없습니다.

* **Question 6**. Why do you need the root privilege to run the programs that use raw sockets? Where does the program fail if executed without the root privilege?
 원시 소켓을 이용하여 패킷을 스푸핑하고 임의 값을 패킷 헤더의 필드에 설정할 수 있습니다. 그래서 해당 작업을 실행하기 위해서는 루트 권한이 필요합니다.
## Task 2.3:Sniff and then Spoof

-코드를 수정하여 실행하였습니다. ping을 보내자 echo요청을 하였습니다. Wireshark를 이용하여 확인 할 수 있었습니다. (task2.3.c, task2.3.txt)


## Submission


