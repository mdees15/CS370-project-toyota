[Link to specification](https://www-sd-nf.oss-cn-beijing.aliyuncs.com/%E5%AE%98%E7%BD%91%E4%B8%8B%E8%BD%BD/SDS011%20laser%20PM2.5%20sensor%20specification-V1.4.pdf)

Each packet has 10 bytes.


| Index | Name | Content |
| :---: | :--: | :-----: |
| 0 | Header | AA |
| 1 | ??? | C0 |
| 2 | DATA1 | Lower byte of PM2.5 value |
| 3 | DATA2 | Upper byte of PM2.5 value |
| 4 | DATA3 | Lower byte of PM10 value |
| 5 | DATA4 | Upper byte of PM10 value |
| 6 | DATA5 | ID byte 1? |
| 7 | DATA6 | ID byte 2? |
| 8 | Checksum | DATA1-6 added together |
| 9 | Tail | AB |

PM2.5 value = ((DATA2 * 256) + DATA1) / 10

PM10 value = ((DATA4 * 256) + DATA3) / 10