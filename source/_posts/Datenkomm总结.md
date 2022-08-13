---
title: Datenkomm 总结
date: 2022-08-12 22:44:45
categories : 
- rwth 
- Datenkomm
tags:
password: cocovv
---
# Datenkomm 22.8 记录
![1](https://github.com/qqxy8/tuchuang/blob/main/006DgsQsly1ftjxmwkbtyj30ub11unpd.jpg?raw=true )
## 第一遍复习结束
### 目录
 1. [材料总结](https://github.com/qqxy8/rwth)
  
 2. 知识点归纳

#### 课件文件列表:
| 文件名   |  
| :----    | 
|  [Kapitel 1 Einführung](#1)                          |
|  [Kapitel 2 Bitübertragungsschicht](#2)              |   
|  [Kapitel 3 Sicherungsschicht](#3)                   |   
|  [Kapitel 4 Vermittlungsschicht](#4)                 |   
|  [Kapitel 5 Transportschicht](#5)                    |   
|  [Kapitel 6 Internet-Protokolle und Sicherheit](#6)  |   

<p id= "1"></p>

- Kapitel 1 Einführung
  1.Daten,Signal,Information (P4)
    * 数据: 事实的表述  
    * 信号: 通过物理量值的特征性空间和/或时间变化对数据进行物理表示
  2.Dienst,Protokoll (P26)
    ![Dienst](./Datenkomm%E6%80%BB%E7%BB%93/k1/Dienst.PNG)
    分为: Dienstnutzer,Dienstbringer,Zugangspunkte,Dienstprimitive
      * Dienstprimitive (P30)
    ![Dienstpri](./Datenkomm%E6%80%BB%E7%BB%93/k1/Dienstpri.PNG)
      * Dienstablauf (P35)  
    Weg-Zeit-Diagramme
    ![Weg-Zeit](./Datenkomm%E6%80%BB%E7%BB%93/k1/Weg-Zeit.PNG)
      - Bestätigter/unbestätigter Dienst (P36)
      * 是否有回执
      - Dienst und Verbindung (P37)
      - Zustandsübergangsdiagramm (P46)
      ![zu](./Datenkomm%E6%80%BB%E7%BB%93/k1/Zustand.PNG)
  3.Scheinbare & tatsächliche Kommunikation (P49)
      - Horizontale und vertikale Kommunikation
    ![Hv](./Datenkomm%E6%80%BB%E7%BB%93/k1/Hv.PNG)
      - Bsp:Alternating Bit Protocol
    g=0: korrekter Empfang; g=1: Daten verfÃ¤lschtg
  4.Kommunikationsarchitekturen
      - Osi/tcp modell
    ![iso](./Datenkomm%E6%80%BB%E7%BB%93/k1/osi.PNG)
  5.其它
      -

  
  

<p id= "2"></p>

- Kapitel 2 Bitübertragungsschicht
   -  periodischer Signale (P17)
   ![1](./Datenkomm%E6%80%BB%E7%BB%93/k2/per.PNG)
   - Aspekte beim Design
    ![2](./Datenkomm%E6%80%BB%E7%BB%93/k2/Asp.PNG)
   - Leitungscode (P29)
    ![3](./Datenkomm%E6%80%BB%E7%BB%93/k2/code.PNG)

   +4B/5B
   - QAM
    ![4](./Datenkomm%E6%80%BB%E7%BB%93/k2/QAM.PNG)
   - 重要参数
    ![5](./Datenkomm%E6%80%BB%E7%BB%93/k2/par.PNG)
   - 香农 有干扰
    ![6](./Datenkomm%E6%80%BB%E7%BB%93/k2/xiangning.PNG)
   - 采样定理
    ![7](./Datenkomm%E6%80%BB%E7%BB%93/k2/caiyang.PNG)

  2.串流
  ![8](./Datenkomm%E6%80%BB%E7%BB%93/k2/chuan.PNG)



<p id= "3"></p>

- Kapitel 3 Sicherungsschicht


  0.任务

  1.Rahmenbildung 5种

  2.Fehlererkennung/-behandlung und Flusskontrolle错误检测/处理和流量控制
  - Hamming距离
    ![1](./Datenkomm%E6%80%BB%E7%BB%93/k3/Q-L-K.PNG)
  - CRC
    ![2](./Datenkomm%E6%80%BB%E7%BB%93/k3/crc.PNG)
  - Proaktive und reaktive Fehlerbehebung (FEC und ARQ)主动和被动的错误恢复
    - Automatic Repeat Request (ARQ) 自动重复请求（ARQ）
      ![3](./Datenkomm%E6%80%BB%E7%BB%93/k3/arq.PNG)
    - Error correcting codes(Forward Error Correction, FEC)(前向纠错，FEC)
      ![4](./Datenkomm%E6%80%BB%E7%BB%93/k3/fec.PNG)
  - Flusskontrolle durch Sliding Window滑动窗口进行流量控制
  3.Medienzugriff
  - Topologien
  ![5](./Datenkomm%E6%80%BB%E7%BB%93/k3/verbindung.PNG)
  - hub switch router

  - Token Passing
  ![6](./Datenkomm%E6%80%BB%E7%BB%93/k3/token.PNG)
  - CSMA/CD
  ![7](./Datenkomm%E6%80%BB%E7%BB%93/k3/csma1.PNG)
  ![8](./Datenkomm%E6%80%BB%E7%BB%93/k3/csma2.PNG)
  4.Ethernet


<p id= "4"></p>

- Kapitel 4 Vermittlungsschicht
  - Vermittlungsverfahren  
    Leitungsvermittlung, Speicher-/Paketvermittlung
    ![1](./Datenkomm%E6%80%BB%E7%BB%93/k4/vermittlung.PNG)
  - Die Vermittlungsschicht im Internet 
    ![2](./Datenkomm%E6%80%BB%E7%BB%93/k4/ipv4.PNG)
    - IPv4: Adressen, Subnetze, CIDR, NAT
  	  ![3](./Datenkomm%E6%80%BB%E7%BB%93/k4/adressklassen.PNG)
      ![4](./Datenkomm%E6%80%BB%E7%BB%93/k4/CIDR.PNG)
      ![5](./Datenkomm%E6%80%BB%E7%BB%93/k4/nat.PNG)
      ![6](./Datenkomm%E6%80%BB%E7%BB%93/k4/nat-bsp.PNG)
    - IPv4-Header
      ![7](./Datenkomm%E6%80%BB%E7%BB%93/k4/ip1.PNG)
      ![7.1](./Datenkomm%E6%80%BB%E7%BB%93/k4/ip2.PNG)
      ![7.2](./Datenkomm%E6%80%BB%E7%BB%93/k4/ip3.PNG)
    - Hilfsprotokolle: ARP, DHCP, ICMP
      ![8](./Datenkomm%E6%80%BB%E7%BB%93/k4/arp.PNG)
      ![9](./Datenkomm%E6%80%BB%E7%BB%93/k4/dhcp.PNG)
      ![10](./Datenkomm%E6%80%BB%E7%BB%93/k4/icmp.PNG)
  - Wegewahlverfahren (Routing)
    - Hierarchien, einfache Verfahren
      ![11]()
    - Distance Vector
      ![12]()
    - Link State
      ![13]()
<p id= "5"></p>

- Kapitel 5 Transportschicht

- Die Transportschicht im Internet
  - TCP (Transmission Control Protocol)
    - Adressierung, Sockets
    - TCP-Verbindung
    - Flusskontrolle
    - TCP-Header
    - Staukontrolle (Congestion Control)
  - UDP (User Datagram Protocol)
<p id= "6"></p>

- Kapitel 6 Internet-Protokolle und Sicherheit
  - Grundlagen der Sicherheit
    -	Sicherheitsprobleme und -ziele安全问题和目标
    -	Symmetrische und asymmetrische Verschlüsselung对称和非对称加密
    -	Authentifizierung
  -  Sichere Internet-Protokolle 网络层安全的互联网协议
    - Vermittlungsschicht: IPSec, IKe
    - Transportschicht: TLS传输层
  - Schutz von lokalen Netzen
    - Firewalls: Packet Filter, Application Gateways