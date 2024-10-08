from datetime import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class FileModel (BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    # date: datetime = Field(default_factory= datetime.now(), alias="date")
    date: datetime = Field(default_factory=datetime.now, alias="date")
    analysis_id: str = Field(...)
    hash_id: str = Field(...)
    filename: str
    type: str
    meta: Optional[dict] = Field(default={})

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "date": "2024-01-17",
                "analysis_id": "YmEzYTRjZDNlYjkxYzI2NmZmM2ZjM2Q1ZTAwYjBhZWQ6MTcwNTQ3OTU2MA==",
                "hash_id": "8a4fcedf21ffef7fe9a267a1398d0fae257997b3446c86bd2f7f7a4ea43be45b",
                "filename": "test.js",
                "type": "malicious",
                "meta":{
        "attributes": {
          "type_description": "JavaScript",
          "tlsh": "T1544112E418F5A51632BF2A7E3A7E60017F6512F52405CA2130DCFAD0AFB4245DEE84FA",
          "vhash": "ab0e339335c49cdd67586ad1f824bc66",
          "type_tags": [
            "source",
            "javascript",
            "js"
          ],
          "names": [
            "forbes_magecart_skimmer.js",
            "forbes_magecart_skimmer - Copy.js",
            "Forbes magecart skimmer_payload.js"
          ],
          "last_modification_date": 1705479560,
          "type_tag": "javascript",
          "times_submitted": 40,
          "total_votes": {
            "harmless": 0,
            "malicious": 0
          },
          "size": 2104,
          "popular_threat_classification": {
            "suggested_threat_label": "phishing.",
            "popular_threat_category": [
              {
                "count": 4,
                "value": "phishing"
              }
            ]
          },
          "last_submission_date": 1705479560,
          "last_analysis_results": {
            "Bkav": {
              "category": "undetected",
              "engine_name": "Bkav",
              "engine_version": "2.0.0.1",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Lionic": {
              "category": "undetected",
              "engine_name": "Lionic",
              "engine_version": "7.5",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Elastic": {
              "category": "type-unsupported",
              "engine_name": "Elastic",
              "engine_version": "4.0.125",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "MicroWorld-eScan": {
              "category": "undetected",
              "engine_name": "MicroWorld-eScan",
              "engine_version": "14.0.409.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "ClamAV": {
              "category": "undetected",
              "engine_name": "ClamAV",
              "engine_version": "1.2.1.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "CMC": {
              "category": "undetected",
              "engine_name": "CMC",
              "engine_version": "2.4.2022.1",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240106"
            },
            "CAT-QuickHeal": {
              "category": "undetected",
              "engine_name": "CAT-QuickHeal",
              "engine_version": "22.00",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "Skyhigh": {
              "category": "undetected",
              "engine_name": "Skyhigh",
              "engine_version": "v2021.2.0+4045",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "McAfee": {
              "category": "undetected",
              "engine_name": "McAfee",
              "engine_version": "6.0.6.653",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Malwarebytes": {
              "category": "undetected",
              "engine_name": "Malwarebytes",
              "engine_version": "4.5.5.54",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Zillya": {
              "category": "undetected",
              "engine_name": "Zillya",
              "engine_version": "2.0.0.5034",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "Sangfor": {
              "category": "undetected",
              "engine_name": "Sangfor",
              "engine_version": "2.23.0.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "K7AntiVirus": {
              "category": "undetected",
              "engine_name": "K7AntiVirus",
              "engine_version": "12.135.50750",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Alibaba": {
              "category": "type-unsupported",
              "engine_name": "Alibaba",
              "engine_version": "0.3.0.5",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20190527"
            },
            "K7GW": {
              "category": "undetected",
              "engine_name": "K7GW",
              "engine_version": "12.135.50749",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Trustlook": {
              "category": "type-unsupported",
              "engine_name": "Trustlook",
              "engine_version": "1.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Baidu": {
              "category": "undetected",
              "engine_name": "Baidu",
              "engine_version": "1.0.0.2",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20190318"
            },
            "VirIT": {
              "category": "undetected",
              "engine_name": "VirIT",
              "engine_version": "9.5.618",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "SymantecMobileInsight": {
              "category": "type-unsupported",
              "engine_name": "SymantecMobileInsight",
              "engine_version": "2.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240103"
            },
            "Symantec": {
              "category": "undetected",
              "engine_name": "Symantec",
              "engine_version": "1.21.0.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "tehtris": {
              "category": "type-unsupported",
              "engine_name": "tehtris",
              "engine_version": "null",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "ESET-NOD32": {
              "category": "undetected",
              "engine_name": "ESET-NOD32",
              "engine_version": "28577",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "APEX": {
              "category": "type-unsupported",
              "engine_name": "APEX",
              "engine_version": "6.490",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "TrendMicro-HouseCall": {
              "category": "undetected",
              "engine_name": "TrendMicro-HouseCall",
              "engine_version": "10.0.0.1040",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Avast": {
              "category": "malicious",
              "engine_name": "Avast",
              "engine_version": "23.9.8494.0",
              "result": "JS:Phishing-CR [Phish]",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Cynet": {
              "category": "undetected",
              "engine_name": "Cynet",
              "engine_version": "4.0.0.28",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Kaspersky": {
              "category": "undetected",
              "engine_name": "Kaspersky",
              "engine_version": "22.0.1.28",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "BitDefender": {
              "category": "undetected",
              "engine_name": "BitDefender",
              "engine_version": "7.2",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "NANO-Antivirus": {
              "category": "undetected",
              "engine_name": "NANO-Antivirus",
              "engine_version": "1.0.146.25796",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "SUPERAntiSpyware": {
              "category": "undetected",
              "engine_name": "SUPERAntiSpyware",
              "engine_version": "5.6.0.1032",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Tencent": {
              "category": "undetected",
              "engine_name": "Tencent",
              "engine_version": "1.0.0.1",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Emsisoft": {
              "category": "undetected",
              "engine_name": "Emsisoft",
              "engine_version": "2022.6.0.32461",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "F-Secure": {
              "category": "undetected",
              "engine_name": "F-Secure",
              "engine_version": "18.10.1547.307",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "DrWeb": {
              "category": "undetected",
              "engine_name": "DrWeb",
              "engine_version": "7.0.61.8090",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "VIPRE": {
              "category": "undetected",
              "engine_name": "VIPRE",
              "engine_version": "6.0.0.35",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "TrendMicro": {
              "category": "undetected",
              "engine_name": "TrendMicro",
              "engine_version": "11.0.0.1006",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "SentinelOne": {
              "category": "type-unsupported",
              "engine_name": "SentinelOne",
              "engine_version": "23.4.2.3",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20231119"
            },
            "Sophos": {
              "category": "undetected",
              "engine_name": "Sophos",
              "engine_version": "2.4.3.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Paloalto": {
              "category": "type-unsupported",
              "engine_name": "Paloalto",
              "engine_version": "0.9.0.1003",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "GData": {
              "category": "undetected",
              "engine_name": "GData",
              "engine_version": "A:25.37175B:27.34584",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Jiangmin": {
              "category": "undetected",
              "engine_name": "Jiangmin",
              "engine_version": "16.0.100",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Webroot": {
              "category": "type-unsupported",
              "engine_name": "Webroot",
              "engine_version": "1.0.0.403",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Varist": {
              "category": "undetected",
              "engine_name": "Varist",
              "engine_version": "6.5.1.2",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Avira": {
              "category": "undetected",
              "engine_name": "Avira",
              "engine_version": "8.3.3.16",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Antiy-AVL": {
              "category": "undetected",
              "engine_name": "Antiy-AVL",
              "engine_version": "3.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Kingsoft": {
              "category": "undetected",
              "engine_name": "Kingsoft",
              "engine_version": "None",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20230906"
            },
            "Gridinsoft": {
              "category": "undetected",
              "engine_name": "Gridinsoft",
              "engine_version": "1.0.155.174",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Xcitium": {
              "category": "undetected",
              "engine_name": "Xcitium",
              "engine_version": "36350",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "Arcabit": {
              "category": "undetected",
              "engine_name": "Arcabit",
              "engine_version": "2022.0.0.18",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "ViRobot": {
              "category": "undetected",
              "engine_name": "ViRobot",
              "engine_version": "2014.3.20.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "ZoneAlarm": {
              "category": "malicious",
              "engine_name": "ZoneAlarm",
              "engine_version": "1.0",
              "result": "HEUR:Trojan-PSW.Script.Generic",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Avast-Mobile": {
              "category": "type-unsupported",
              "engine_name": "Avast-Mobile",
              "engine_version": "240116-02",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Microsoft": {
              "category": "undetected",
              "engine_name": "Microsoft",
              "engine_version": "1.1.23110.2",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Google": {
              "category": "undetected",
              "engine_name": "Google",
              "engine_version": "1705402827",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "BitDefenderFalx": {
              "category": "type-unsupported",
              "engine_name": "BitDefenderFalx",
              "engine_version": "2.0.936",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240108"
            },
            "AhnLab-V3": {
              "category": "undetected",
              "engine_name": "AhnLab-V3",
              "engine_version": "3.25.0.10459",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Acronis": {
              "category": "undetected",
              "engine_name": "Acronis",
              "engine_version": "1.2.0.121",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20230828"
            },
            "BitDefenderTheta": {
              "category": "undetected",
              "engine_name": "BitDefenderTheta",
              "engine_version": "7.2.37796.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240103"
            },
            "ALYac": {
              "category": "undetected",
              "engine_name": "ALYac",
              "engine_version": "2.0.0.8",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "TACHYON": {
              "category": "undetected",
              "engine_name": "TACHYON",
              "engine_version": "2024-01-16.02",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "DeepInstinct": {
              "category": "type-unsupported",
              "engine_name": "DeepInstinct",
              "engine_version": "5.0.0.8",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "VBA32": {
              "category": "undetected",
              "engine_name": "VBA32",
              "engine_version": "5.0.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Cylance": {
              "category": "type-unsupported",
              "engine_name": "Cylance",
              "engine_version": "2.0.0.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240103"
            },
            "Zoner": {
              "category": "undetected",
              "engine_name": "Zoner",
              "engine_version": "2.2.2.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Rising": {
              "category": "undetected",
              "engine_name": "Rising",
              "engine_version": "25.0.0.27",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Yandex": {
              "category": "undetected",
              "engine_name": "Yandex",
              "engine_version": "5.5.2.24",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Ikarus": {
              "category": "undetected",
              "engine_name": "Ikarus",
              "engine_version": "6.2.4.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "MaxSecure": {
              "category": "undetected",
              "engine_name": "MaxSecure",
              "engine_version": "1.0.0.1",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Fortinet": {
              "category": "undetected",
              "engine_name": "Fortinet",
              "engine_version": "None",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "AVG": {
              "category": "malicious",
              "engine_name": "AVG",
              "engine_version": "23.9.8494.0",
              "result": "JS:Phishing-CR [Phish]",
              "method": "blacklist",
              "engine_update": "20240116"
            },
            "Cybereason": {
              "category": "type-unsupported",
              "engine_name": "Cybereason",
              "engine_version": "1.2.449",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20231102"
            },
            "Panda": {
              "category": "undetected",
              "engine_name": "Panda",
              "engine_version": "4.6.4.2",
              "result": "null",
              "method": "blacklist",
              "engine_update": "20240115"
            },
            "CrowdStrike": {
              "category": "type-unsupported",
              "engine_name": "CrowdStrike",
              "engine_version": "1.0",
              "result": "null",
              "method": "blacklist",
              "engine_update": "null"
            }
          },
          "sha256": "8a4fcedf21ffef7fe9a267a1398d0fae257997b3446c86bd2f7f7a4ea43be45b",
          "type_extension": "js",
          "tags": [
            "javascript"
          ],
          "last_analysis_date": 1705406317,
          "unique_sources": 3,
          "first_submission_date": 1589789709,
          "ssdeep": "24:9QWYEz2vgR2ktmy9mOphriAxiHR09oO+Ah3+ex2Agd5u4E5I17NCFWaL:VtlRPtBmTRHR06k1xlgd5xmWY",
          "md5": "ba3a4cd3eb91c266ff3fc3d5e00b0aed",
          "sha1": "9b1cadc71c33808c8e54d3595fc6053567718cc6",
          "magic": "ASCII text",
          "last_analysis_stats": {
            "harmless": 0,
            "type-unsupported": 15,
            "suspicious": 0,
            "confirmed-timeout": 0,
            "timeout": 0,
            "failure": 0,
            "malicious": 3,
            "undetected": 55
          },
          "meaningful_name": "forbes_magecart_skimmer.js",
          "reputation": 0
        },
        "type": "file",
        "id": "8a4fcedf21ffef7fe9a267a1398d0fae257997b3446c86bd2f7f7a4ea43be45b",
        "links": {
          "self": "https://www.virustotal.com/api/v3/files/8a4fcedf21ffef7fe9a267a1398d0fae257997b3446c86bd2f7f7a4ea43be45b"
        }
      }
            }
        }