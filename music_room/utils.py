import random
import json

random_data = {
    "objects": [
        {
            "song_id": "W775nQuxOwY",
            "song_name": "Lauv - Drugs & The Internet [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/W775nQuxOwY/maxresdefault.webp"
            },
            "duration": 232,
            "like_count": 178812,
            "dislike_count": 2545,
            "artist": "Lauv"
        },
        {
            "song_id": "_cmORZMgv6I",
            "song_name": "Lauv - ****, i'm lonely (with Anne-Marie) [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/_cmORZMgv6I/maxresdefault.webp?v=5d5daf31"
            },
            "duration": 197,
            "like_count": 634100,
            "dislike_count": 8894,
            "artist": "Lauv"
        },
        {
            "song_id": "1lRGr4rSCz4",
            "song_name": "Lauv - Lonely Eyes [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/1lRGr4rSCz4/maxresdefault.webp"
            },
            "duration": 197,
            "like_count": 84426,
            "dislike_count": 398,
            "artist": "Lauv"
        },
        {
            "song_id": "36IMLszdhD4",
            "song_name": "Lauv - \"Sims\" [Official Short Film]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/36IMLszdhD4/maxresdefault.webp?v=5db63da7"
            },
            "duration": 281,
            "like_count": 73454,
            "dislike_count": 838,
            "artist": "Lauv"
        },
        {
            "song_id": "lVU7YGdmtMo",
            "song_name": "Believed",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/lVU7YGdmtMo/maxresdefault.webp"
            },
            "duration": 170,
            "like_count": 4758,
            "dislike_count": 503,
            "artist": "Lauv"
        },
        {
            "song_id": "xzeZt9WqmGg",
            "song_name": "Lauv - Billy [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/xzeZt9WqmGg/maxresdefault.webp"
            },
            "duration": 180,
            "like_count": 26664,
            "dislike_count": 112,
            "artist": "Lauv"
        },
        {
            "song_id": "2k5w6eTxGXk",
            "song_name": "Lauv - Feelings [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/2k5w6eTxGXk/maxresdefault.webp?v=5d82853b"
            },
            "duration": 184,
            "like_count": 221522,
            "dislike_count": 2260,
            "artist": "Lauv"
        },
        {
            "song_id": "hb_p3bKrK84",
            "song_name": "Lauv - Canada (feat. Alessia Cara) [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/hb_p3bKrK84/maxresdefault.webp"
            },
            "duration": 184,
            "like_count": 44322,
            "dislike_count": 495,
            "artist": "Lauv"
        },
        {
            "song_id": "xbX9bXshKr0",
            "song_name": "Lauv - For Now [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/xbX9bXshKr0/maxresdefault.webp"
            },
            "duration": 188,
            "like_count": 35823,
            "dislike_count": 176,
            "artist": "Lauv"
        },
        {
            "song_id": "c_10qS7amjk",
            "song_name": "Lauv & LANY - Mean It [Official Video]",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/c_10qS7amjk/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDenK2xfSrMrzgeTmA5-Qg609rDjA"
            },
            "duration": 236,
            "like_count": 591047,
            "dislike_count": 5897,
            "artist": "Lauv, LANY"
        },
        {
            "song_id": "Plq2g3_OojE",
            "song_name": "Lauv - Tell My Mama [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/Plq2g3_OojE/maxresdefault.webp"
            },
            "duration": 169,
            "like_count": 18381,
            "dislike_count": 91,
            "artist": "Lauv"
        },
        {
            "song_id": "UIhrtnwLA60",
            "song_name": "Lauv - Sweatpants [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/UIhrtnwLA60/maxresdefault.webp"
            },
            "duration": 195,
            "like_count": 18328,
            "dislike_count": 127,
            "artist": "Lauv"
        },
        {
            "song_id": "vS0YXAfUo4k",
            "song_name": "Lauv - Who (feat. BTS) [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/vS0YXAfUo4k/maxresdefault.webp"
            },
            "duration": 180,
            "like_count": 1429946,
            "dislike_count": 9913,
            "artist": "Lauv"
        },
        {
            "song_id": "boUl0jPZMdg",
            "song_name": "Lauv & Troye Sivan - i'm so tired... [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/boUl0jPZMdg/maxresdefault.webp?v=5c5e037d"
            },
            "duration": 172,
            "like_count": 408197,
            "dislike_count": 5233,
            "artist": "LAUV"
        },
        {
            "song_id": "qhuJpbqXxDo",
            "song_name": "Lauv - El Tejano (feat. Sof\u00eda Reyes) [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/qhuJpbqXxDo/maxresdefault.webp?v=5ebc5b3d"
            },
            "duration": 248,
            "like_count": 147370,
            "dislike_count": 1323,
            "artist": "Lauv"
        },
        {
            "song_id": "j9DnUII28fI",
            "song_name": "Lauv - Tattoos Together [Official Video]",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/j9DnUII28fI/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBGwjO6zD8ru0O7Mxkaeb23rcOqIg"
            },
            "duration": 237,
            "like_count": 254359,
            "dislike_count": 3084,
            "artist": "Lauv"
        },
        {
            "song_id": "pPAAFMtDUzo",
            "song_name": "Lauv - Changes [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/pPAAFMtDUzo/maxresdefault.webp"
            },
            "duration": 158,
            "like_count": 312220,
            "dislike_count": 2247,
            "artist": "Lauv"
        },
        {
            "song_id": "Klsi8CbSm8Y",
            "song_name": "Lauv - Sad Forever [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/Klsi8CbSm8Y/maxresdefault.webp"
            },
            "duration": 209,
            "like_count": 372254,
            "dislike_count": 2400,
            "artist": "Lauv"
        },
        {
            "song_id": "_lAfQwmjdGU",
            "song_name": "Lauv - Invisible Things [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/_lAfQwmjdGU/maxresdefault.webp?v=5e6146f3"
            },
            "duration": 195,
            "like_count": 73077,
            "dislike_count": 351,
            "artist": "Lauv"
        },
        {
            "song_id": "0PTU4kGj5JI",
            "song_name": "Lauv - Julia [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/0PTU4kGj5JI/maxresdefault.webp"
            },
            "duration": 218,
            "like_count": 98306,
            "dislike_count": 563,
            "artist": "Lauv"
        },
        {
            "song_id": "bDidwMxir4o",
            "song_name": "Lauv - Modern Loneliness [Official Visualizer]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/bDidwMxir4o/maxresdefault.webp?v=5e4c5ea5"
            },
            "duration": 247,
            "like_count": 329078,
            "dislike_count": 2700,
            "artist": "Lauv"
        },
        {
            "song_id": "RsEZmictANA",
            "song_name": "Taylor Swift - willow (Official Music Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/RsEZmictANA/maxresdefault.jpg?v=5fd2fe5a"
            },
            "duration": 253,
            "like_count": 1713362,
            "dislike_count": 33062,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "wMpqCRF7TKg",
            "song_name": "Taylor Swift - champagne problems (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/wMpqCRF7TKg/maxresdefault.jpg"
            },
            "duration": 248,
            "like_count": 324687,
            "dislike_count": 3336,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "Pz-f9mM3Ms8",
            "song_name": "Taylor Swift - gold rush (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/Pz-f9mM3Ms8/maxresdefault.jpg"
            },
            "duration": 188,
            "like_count": 179377,
            "dislike_count": 1140,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "WuvhOD-mP8M",
            "song_name": "Taylor Swift - \u2018tis the damn season (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/WuvhOD-mP8M/maxresdefault.jpg"
            },
            "duration": 235,
            "like_count": 150102,
            "dislike_count": 1107,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "ukxEKY_7MOc",
            "song_name": "Taylor Swift - tolerate it (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/ukxEKY_7MOc/maxresdefault.jpg"
            },
            "duration": 247,
            "like_count": 151610,
            "dislike_count": 883,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "IEPomqor2A8",
            "song_name": "Taylor Swift - no body, no crime (Official Lyric Video) ft. HAIM",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/IEPomqor2A8/maxresdefault.jpg"
            },
            "duration": 218,
            "like_count": 276921,
            "dislike_count": 2000,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "tP4TTgt4nb0",
            "song_name": "Taylor Swift - happiness (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/tP4TTgt4nb0/maxresdefault.jpg"
            },
            "duration": 317,
            "like_count": 140474,
            "dislike_count": 839,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "zI4DS5GmQWE",
            "song_name": "Taylor Swift - dorothea (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/zI4DS5GmQWE/maxresdefault.jpg"
            },
            "duration": 225,
            "like_count": 181858,
            "dislike_count": 1223,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "c_p_TBaHvos",
            "song_name": "Taylor Swift - coney island (Lyric Video) ft. The National",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/c_p_TBaHvos/maxresdefault.jpg"
            },
            "duration": 278,
            "like_count": 121151,
            "dislike_count": 774,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "9nIOx-ezlzA",
            "song_name": "Taylor Swift - ivy (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/9nIOx-ezlzA/maxresdefault.jpg"
            },
            "duration": 258,
            "like_count": 126720,
            "dislike_count": 702,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "YPlNBb6I8qU",
            "song_name": "Taylor Swift - cowboy like me (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/YPlNBb6I8qU/maxresdefault.jpg"
            },
            "duration": 280,
            "like_count": 113000,
            "dislike_count": 859,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "rqQHa2HcGtM",
            "song_name": "Taylor Swift - long story short (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/rqQHa2HcGtM/maxresdefault.jpg"
            },
            "duration": 221,
            "like_count": 139958,
            "dislike_count": 604,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "hP6QpMeSG6s",
            "song_name": "Taylor Swift - marjorie (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/hP6QpMeSG6s/maxresdefault.jpg"
            },
            "duration": 258,
            "like_count": 205025,
            "dislike_count": 745,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "AIFnKqIeEdY",
            "song_name": "Taylor Swift - closure (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/AIFnKqIeEdY/maxresdefault.jpg"
            },
            "duration": 183,
            "like_count": 106373,
            "dislike_count": 779,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "EXLgZZE072g",
            "song_name": "Taylor Swift - evermore (Official Lyric Video) ft. Bon Iver",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/EXLgZZE072g/maxresdefault.jpg"
            },
            "duration": 304,
            "like_count": 269395,
            "dislike_count": 2451,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "wIft-t-MQuE",
            "song_name": "Taylor Swift - \u2026Ready For It?",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/wIft-t-MQuE/maxresdefault.jpg"
            },
            "duration": 211,
            "like_count": 3261451,
            "dislike_count": 237830,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "dfnCAmr569k",
            "song_name": "Taylor Swift - End Game ft. Ed Sheeran, Future",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/dfnCAmr569k/maxresdefault.jpg"
            },
            "duration": 251,
            "like_count": 2981520,
            "dislike_count": 162489,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "xYLxUJ9v6KU",
            "song_name": "I Did Something Bad",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/xYLxUJ9v6KU/maxresdefault.webp"
            },
            "duration": 238,
            "like_count": 79239,
            "dislike_count": 3973,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "kRJKB291Z1g",
            "song_name": "Don\u2019t Blame Me",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/kRJKB291Z1g/maxresdefault.webp"
            },
            "duration": 236,
            "like_count": 68638,
            "dislike_count": 3295,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "tCXGJQYZ9JA",
            "song_name": "Taylor Swift - Delicate",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/tCXGJQYZ9JA/maxresdefault.jpg"
            },
            "duration": 235,
            "like_count": 3751357,
            "dislike_count": 215646,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "3tmd-ClpJxA",
            "song_name": "Taylor Swift - Look What You Made Me Do",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/3tmd-ClpJxA/maxresdefault.jpg"
            },
            "duration": 256,
            "like_count": 10649968,
            "dislike_count": 1319960,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "iAv1Y1YIwm8",
            "song_name": "So It Goes...",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/iAv1Y1YIwm8/maxresdefault.webp"
            },
            "duration": 228,
            "like_count": 29860,
            "dislike_count": 1711,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "EUoe7cf0HYw",
            "song_name": "Taylor Swift - Gorgeous (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/EUoe7cf0HYw/maxresdefault.jpg"
            },
            "duration": 212,
            "like_count": 1185443,
            "dislike_count": 63869,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "FhPLQVlUiNQ",
            "song_name": "Getaway Car",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/FhPLQVlUiNQ/maxresdefault.webp"
            },
            "duration": 234,
            "like_count": 52774,
            "dislike_count": 1868,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "5U7bF68xcRg",
            "song_name": "King Of My Heart",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/5U7bF68xcRg/maxresdefault.webp"
            },
            "duration": 214,
            "like_count": 40667,
            "dislike_count": 2183,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "erGyUphZSt8",
            "song_name": "Dancing With Our Hands Tied",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/erGyUphZSt8/maxresdefault.webp"
            },
            "duration": 212,
            "like_count": 27549,
            "dislike_count": 1569,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "FNEoPctNIUE",
            "song_name": "Dress",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/FNEoPctNIUE/maxresdefault.webp"
            },
            "duration": 230,
            "like_count": 25490,
            "dislike_count": 1628,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "6Z3QJ4L1Bg0",
            "song_name": "This Is Why We Can't Have Nice Things",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/6Z3QJ4L1Bg0/maxresdefault.webp"
            },
            "duration": 207,
            "like_count": 36205,
            "dislike_count": 2288,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "V54CEElTF_U",
            "song_name": "Taylor Swift - Call It What You Want (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/V54CEElTF_U/maxresdefault.jpg"
            },
            "duration": 206,
            "like_count": 971180,
            "dislike_count": 29690,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "KkvTYrFIxNM",
            "song_name": "New Year\u2019s Day",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/KkvTYrFIxNM/maxresdefault.webp"
            },
            "duration": 235,
            "like_count": 26396,
            "dislike_count": 2399,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "p1cEvNn88jM",
            "song_name": "Taylor Swift - I Forgot That You Existed (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/p1cEvNn88jM/maxresdefault.jpg"
            },
            "duration": 172,
            "like_count": 217671,
            "dislike_count": 3370,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "ic8j13piAhQ",
            "song_name": "Taylor Swift - Cruel Summer (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/ic8j13piAhQ/maxresdefault.jpg"
            },
            "duration": 179,
            "like_count": 273899,
            "dislike_count": 4566,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "-BjZmE2gtdo",
            "song_name": "Taylor Swift - Lover",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/-BjZmE2gtdo/maxresdefault.jpg?v=5fdd01b5"
            },
            "duration": 238,
            "like_count": 2408087,
            "dislike_count": 98429,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "AqAJLh9wuZ0",
            "song_name": "Taylor Swift - The Man (Official Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/AqAJLh9wuZ0/maxresdefault.jpg?v=5fdd01e3"
            },
            "duration": 255,
            "like_count": 1548425,
            "dislike_count": 167117,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "8KpKc3C9V3w",
            "song_name": "Taylor Swift - The Archer (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/8KpKc3C9V3w/maxresdefault.jpg"
            },
            "duration": 219,
            "like_count": 587614,
            "dislike_count": 19319,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "2d1wKn-oJnA",
            "song_name": "Taylor Swift - I Think He Knows (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/2d1wKn-oJnA/maxresdefault.jpg"
            },
            "duration": 174,
            "like_count": 130236,
            "dislike_count": 1477,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "Kwf7P2GNAVw",
            "song_name": "Taylor Swift - Miss Americana & The Heartbreak Prince (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/Kwf7P2GNAVw/maxresdefault.jpg"
            },
            "duration": 235,
            "like_count": 186705,
            "dislike_count": 1892,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "8zdg-pDF10g",
            "song_name": "Taylor Swift - Paper Rings (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/8zdg-pDF10g/maxresdefault.jpg"
            },
            "duration": 223,
            "like_count": 162443,
            "dislike_count": 2016,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "VikHHWrgb4Y",
            "song_name": "Taylor Swift - Cornelia Street (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/VikHHWrgb4Y/maxresdefault.jpg"
            },
            "duration": 288,
            "like_count": 167019,
            "dislike_count": 2082,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "GTEFSuFfgnU",
            "song_name": "Taylor Swift - Death By A Thousand Cuts (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/GTEFSuFfgnU/maxresdefault.jpg"
            },
            "duration": 200,
            "like_count": 101696,
            "dislike_count": 1018,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "VsKoOH6DVys",
            "song_name": "Taylor Swift - London Boy (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/VsKoOH6DVys/maxresdefault.jpg"
            },
            "duration": 191,
            "like_count": 150268,
            "dislike_count": 2130,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "tMoW5G5LU08",
            "song_name": "Taylor Swift - Soon You\u2019ll Get Better (Official Audio) ft. The Chicks",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/tMoW5G5LU08/maxresdefault.jpg"
            },
            "duration": 203,
            "like_count": 123782,
            "dislike_count": 1240,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "acQXa5ArHIk",
            "song_name": "Taylor Swift - False God (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/acQXa5ArHIk/maxresdefault.jpg"
            },
            "duration": 201,
            "like_count": 88365,
            "dislike_count": 1497,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "Dkk9gvTmCXY",
            "song_name": "Taylor Swift - You Need To Calm Down",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/Dkk9gvTmCXY/maxresdefault.jpg?v=5fdd018f"
            },
            "duration": 210,
            "like_count": 3991197,
            "dislike_count": 315738,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "8HxbqAsppwU",
            "song_name": "Taylor Swift - Afterglow (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/8HxbqAsppwU/maxresdefault.jpg"
            },
            "duration": 224,
            "like_count": 135941,
            "dislike_count": 1150,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "FuXNumBwDOM",
            "song_name": "Taylor Swift - ME! (feat. Brendon Urie of Panic! At The Disco)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/FuXNumBwDOM/maxresdefault.webp?v=5fdd011b"
            },
            "duration": 249,
            "like_count": 5628852,
            "dislike_count": 398934,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "eaP1VswBF28",
            "song_name": "Taylor Swift - It\u2019s Nice To Have A Friend (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/eaP1VswBF28/maxresdefault.jpg"
            },
            "duration": 152,
            "like_count": 86295,
            "dislike_count": 898,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "u9raS7-NisU",
            "song_name": "Taylor Swift - Daylight (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/u9raS7-NisU/maxresdefault.jpg"
            },
            "duration": 294,
            "like_count": 217818,
            "dislike_count": 2197,
            "artist": "Taylor Swift"
        },        
        {
            "song_id": "KsZ6tROaVOQ",
            "song_name": "Taylor Swift - the 1 (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/KsZ6tROaVOQ/maxresdefault.jpg"
            },
            "duration": 211,
            "like_count": 487612,
            "dislike_count": 7224,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "K-a8s8OLBSE",
            "song_name": "Taylor Swift - cardigan (Official Music Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/K-a8s8OLBSE/maxresdefault.jpg?v=5fdd0796"
            },
            "duration": 275,
            "like_count": 2083432,
            "dislike_count": 54576,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "2s5xdY6MCeI",
            "song_name": "Taylor Swift - the last great american dynasty (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/2s5xdY6MCeI/maxresdefault.jpg"
            },
            "duration": 232,
            "like_count": 261287,
            "dislike_count": 2810,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "osdoLjUNFnA",
            "song_name": "Taylor Swift \u2013 exile (feat. Bon Iver) (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/osdoLjUNFnA/maxresdefault.jpg"
            },
            "duration": 287,
            "like_count": 797713,
            "dislike_count": 12310,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "OWbDJFtHl3w",
            "song_name": "Taylor Swift \u2013 my tears ricochet (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/OWbDJFtHl3w/maxresdefault.jpg"
            },
            "duration": 257,
            "like_count": 260924,
            "dislike_count": 1997,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "KaM1bCuG4xo",
            "song_name": "Taylor Swift \u2013 mirrorball (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/KaM1bCuG4xo/maxresdefault.jpg"
            },
            "duration": 210,
            "like_count": 176240,
            "dislike_count": 1421,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "pEY-GPsru_E",
            "song_name": "Taylor Swift \u2013 seven (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/pEY-GPsru_E/maxresdefault.jpg"
            },
            "duration": 210,
            "like_count": 196633,
            "dislike_count": 1521,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "nn_0zPAfyo8",
            "song_name": "Taylor Swift \u2013 august (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/nn_0zPAfyo8/maxresdefault.jpg"
            },
            "duration": 264,
            "like_count": 377710,
            "dislike_count": 2596,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "9bdLTPNrlEg",
            "song_name": "Taylor Swift \u2013 this is me trying (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/9bdLTPNrlEg/maxresdefault.jpg"
            },
            "duration": 196,
            "like_count": 198455,
            "dislike_count": 1175,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "MLV2SJKWk4M",
            "song_name": "Taylor Swift \u2013 illicit affairs (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/MLV2SJKWk4M/maxresdefault.jpg"
            },
            "duration": 192,
            "like_count": 171372,
            "dislike_count": 1025,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "OuFnpmGwg5k",
            "song_name": "Taylor Swift \u2013 invisible string (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/OuFnpmGwg5k/maxresdefault.jpg"
            },
            "duration": 254,
            "like_count": 221930,
            "dislike_count": 1926,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "6DP4q_1EgQQ",
            "song_name": "Taylor Swift \u2013 mad woman (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/6DP4q_1EgQQ/maxresdefault.jpg"
            },
            "duration": 238,
            "like_count": 197854,
            "dislike_count": 1435,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "DUnDkI7l9LQ",
            "song_name": "Taylor Swift \u2013 epiphany (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/DUnDkI7l9LQ/maxresdefault.jpg"
            },
            "duration": 291,
            "like_count": 177329,
            "dislike_count": 1377,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "gtzCuhDTRzk",
            "song_name": "betty",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/gtzCuhDTRzk/maxresdefault.webp"
            },
            "duration": 295,
            "like_count": 33297,
            "dislike_count": 2928,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "HpxX4ZE4KWE",
            "song_name": "Taylor Swift \u2013 peace (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/HpxX4ZE4KWE/maxresdefault.jpg"
            },
            "duration": 235,
            "like_count": 144218,
            "dislike_count": 1208,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "ryLGxpjwAhM",
            "song_name": "Taylor Swift \u2013 hoax (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/ryLGxpjwAhM/maxresdefault.jpg"
            },
            "duration": 221,
            "like_count": 220562,
            "dislike_count": 1959,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "7lLigiVgJsE",
            "song_name": "Taylor Swift - Fearless (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/7lLigiVgJsE/maxresdefault.jpg"
            },
            "duration": 245,
            "like_count": 118404,
            "dislike_count": 479,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "rLCol1C3ouc",
            "song_name": "Taylor Swift - Fifteen (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/rLCol1C3ouc/maxresdefault.jpg"
            },
            "duration": 295,
            "like_count": 90872,
            "dislike_count": 208,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "aXzVF3XeS8M",
            "song_name": "Taylor Swift - Love Story (Taylor\u2019s Version) [Official Lyric Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/aXzVF3XeS8M/maxresdefault.jpg"
            },
            "duration": 240,
            "like_count": 1219601,
            "dislike_count": 9735,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "tMhiHrL7rPE",
            "song_name": "Taylor Swift - Hey Stephen (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/tMhiHrL7rPE/maxresdefault.jpg"
            },
            "duration": 256,
            "like_count": 56862,
            "dislike_count": 116,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "9-rKvhsjwKU",
            "song_name": "Taylor Swift - White Horse (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/9-rKvhsjwKU/maxresdefault.jpg"
            },
            "duration": 239,
            "like_count": 86357,
            "dislike_count": 165,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "vwp8Ur6tO-8",
            "song_name": "Taylor Swift - You Belong With Me (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/vwp8Ur6tO-8/maxresdefault.jpg"
            },
            "duration": 232,
            "like_count": 208703,
            "dislike_count": 569,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "qsUK-BG5OQQ",
            "song_name": "Taylor Swift - Breathe (Taylor's Version) (Lyric Video) ft. Colbie Caillat",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/qsUK-BG5OQQ/maxresdefault.jpg"
            },
            "duration": 266,
            "like_count": 56865,
            "dislike_count": 114,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "cwFbq-70EwE",
            "song_name": "Taylor Swift - Tell Me Why (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/cwFbq-70EwE/maxresdefault.jpg"
            },
            "duration": 202,
            "like_count": 34585,
            "dislike_count": 41,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "DNaSlUYIXBg",
            "song_name": "Taylor Swift - You're Not Sorry (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/DNaSlUYIXBg/maxresdefault.jpg"
            },
            "duration": 262,
            "like_count": 51233,
            "dislike_count": 76,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "DlexmDDSDZ0",
            "song_name": "Taylor Swift - The Way I Loved You (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/DlexmDDSDZ0/maxresdefault.jpg"
            },
            "duration": 246,
            "like_count": 72834,
            "dislike_count": 129,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "T-41vMWQTUA",
            "song_name": "Taylor Swift - Forever & Always (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/T-41vMWQTUA/maxresdefault.jpg"
            },
            "duration": 225,
            "like_count": 46111,
            "dislike_count": 93,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "KZeI9I875Ig",
            "song_name": "Taylor Swift - The Best Day (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/KZeI9I875Ig/maxresdefault.jpg"
            },
            "duration": 249,
            "like_count": 70535,
            "dislike_count": 88,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "jwWR1cQTKyw",
            "song_name": "Taylor Swift - Change (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/jwWR1cQTKyw/maxresdefault.jpg"
            },
            "duration": 278,
            "like_count": 34774,
            "dislike_count": 56,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "vUHDR6Rg3Y4",
            "song_name": "Taylor Swift - Jump Then Fall (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/vUHDR6Rg3Y4/maxresdefault.jpg"
            },
            "duration": 238,
            "like_count": 36056,
            "dislike_count": 57,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "8bNlGwnEUAs",
            "song_name": "Taylor Swift - Untouchable (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/8bNlGwnEUAs/maxresdefault.jpg"
            },
            "duration": 315,
            "like_count": 42596,
            "dislike_count": 66,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "RcGowZ26sE0",
            "song_name": "Taylor Swift - Forever & Always (Piano Version) (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/RcGowZ26sE0/maxresdefault.jpg"
            },
            "duration": 272,
            "like_count": 34869,
            "dislike_count": 41,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "ePjcjLRHPOo",
            "song_name": "Taylor Swift - Come In With The Rain (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/ePjcjLRHPOo/maxresdefault.jpg"
            },
            "duration": 237,
            "like_count": 28621,
            "dislike_count": 31,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "IsCik8wznlU",
            "song_name": "Taylor Swift - Superstar (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/IsCik8wznlU/maxresdefault.jpg"
            },
            "duration": 264,
            "like_count": 32342,
            "dislike_count": 53,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "425n1NoRtgA",
            "song_name": "Taylor Swift - The Other Side Of The Door (Taylor\u2019s Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/425n1NoRtgA/maxresdefault.jpg"
            },
            "duration": 238,
            "like_count": 29142,
            "dislike_count": 22,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "xSWVPqnKcXQ",
            "song_name": "Taylor Swift - Today Was A Fairytale (Taylor's Version) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/xSWVPqnKcXQ/maxresdefault.jpg"
            },
            "duration": 242,
            "like_count": 53255,
            "dislike_count": 102,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "XKaMUm7YwZc",
            "song_name": "Taylor Swift ft. Maren Morris - You All Over Me (From The Vault) (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/XKaMUm7YwZc/maxresdefault.jpg"
            },
            "duration": 223,
            "like_count": 327123,
            "dislike_count": 3194,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "rFjJs6ZjPe8",
            "song_name": "Taylor Swift - Mr. Perfectly Fine (Taylor\u2019s Version) (From The Vault) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/rFjJs6ZjPe8/maxresdefault.jpg"
            },
            "duration": 278,
            "like_count": 374347,
            "dislike_count": 3762,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "seU5y5EgIwk",
            "song_name": "Taylor Swift - We Were Happy (Taylor\u2019s Version) (From The Vault)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/seU5y5EgIwk/maxresdefault.jpg"
            },
            "duration": 244,
            "like_count": 57162,
            "dislike_count": 139,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "aOa6D6ku3dM",
            "song_name": "That\u2019s When (Taylor\u2019s Version) (From The Vault) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/aOa6D6ku3dM/maxresdefault.jpg"
            },
            "duration": 191,
            "like_count": 60639,
            "dislike_count": 152,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "dHdAN4FXzmc",
            "song_name": "Taylor Swift - Don\u2019t You (Taylor\u2019s Version) (From The Vault) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/dHdAN4FXzmc/maxresdefault.jpg"
            },
            "duration": 211,
            "like_count": 43840,
            "dislike_count": 73,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "yuFuwXd-B9E",
            "song_name": "Taylor Swift - Bye Bye Baby (Taylor\u2019s Version) (From The Vault) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/yuFuwXd-B9E/maxresdefault.jpg"
            },
            "duration": 244,
            "like_count": 56911,
            "dislike_count": 183,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "FeTHyZJvozc",
            "song_name": "Taylor Swift - Love Story (Elvira Remix) (Taylor\u2019s Version) (Official Audio)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/FeTHyZJvozc/maxresdefault.jpg"
            },
            "duration": 214,
            "like_count": 137507,
            "dislike_count": 701,
            "artist": "Taylor Swift"
        },
        {
            "song_id": "06k5XN78OP0",
            "song_name": "Jeremy Zucker, Chelsea Cutler - you were good to me (Official Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/06k5XN78OP0/maxresdefault.webp"
            },
            "duration": 221,
            "like_count": 252273,
            "dislike_count": 1860,
            "artist": "Jeremy Zucker, Chelsea Cutler"
        },
        {
            "song_id": "aNH5z_tK_sg",
            "song_name": "Jeremy Zucker & Chelsea Cutler - parent song (Official Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/aNH5z_tK_sg/maxresdefault.jpg"
            },
            "duration": 263,
            "like_count": 17090,
            "dislike_count": 84,
            "artist": "Jeremy Zucker, Chelsea Cutler"
        },
        {
            "song_id": "5HzpPl5a9EA",
            "song_name": "Noah Kahan - Anyway",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/5HzpPl5a9EA/maxresdefault.webp"
            },
            "duration": 315,
            "like_count": 78534,
            "dislike_count": 953,
            "artist": "Noah Kahan"
        },
        {
            "song_id": "i-qT5n_5Mys",
            "song_name": "Jaymes Young - Happiest Year [Official Music Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/i-qT5n_5Mys/maxresdefault.webp"
            },
            "duration": 277,
            "like_count": 432587,
            "dislike_count": 3968,
            "artist": "Jaymes Young"
        },
        {
            "song_id": "mak0DkRbuCY",
            "song_name": "Finding Hope - 3:00 AM (Official Music Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/mak0DkRbuCY/maxresdefault.webp"
            },
            "duration": 203,
            "like_count": 134413,
            "dislike_count": 2043,
            "artist": "Finding Hope"
        },
        {
            "song_id": "LoY6nmmjnHM",
            "song_name": "Alexander 23 - IDK You Yet [Lyric Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/LoY6nmmjnHM/maxresdefault.jpg"
            },
            "duration": 186,
            "like_count": 252512,
            "dislike_count": 1008,
            "artist": "Alexander 23"
        },
        {
            "song_id": "kOCkne-Bku4",
            "song_name": "Lauv - Paris in the Rain [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/kOCkne-Bku4/maxresdefault.webp"
            },
            "duration": 217,
            "like_count": 1150150,
            "dislike_count": 13057,
            "artist": "Lauv"
        },
        {
            "song_id": "lY2yjAdbvdQ",
            "song_name": "Shawn Mendes - Treat You Better",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/lY2yjAdbvdQ/maxresdefault.webp"
            },
            "duration": 256,
            "like_count": 9303661,
            "dislike_count": 313984,
            "artist": "Shawn Mendes"
        },
        {
            "song_id": "BcqxLCWn-CE",
            "song_name": "Lauv - I Like Me Better [Official Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/BcqxLCWn-CE/maxresdefault.webp"
            },
            "duration": 205,
            "like_count": 1601508,
            "dislike_count": 24526,
            "artist": "Lauv"
        },
        {
            "song_id": "jO2viLEW-1A",
            "song_name": "Jeremy Zucker - comethru (Official Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/jO2viLEW-1A/maxresdefault.webp"
            },
            "duration": 181,
            "like_count": 4063099,
            "dislike_count": 43996,
            "artist": "Jeremy Zucker"
        },
        {
            "song_id": "NKzd_YiW9AQ",
            "song_name": "Ali Gatie - What If I Told You That I Love You [Official Music Video]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/NKzd_YiW9AQ/maxresdefault.webp"
            },
            "duration": 214,
            "like_count": 1618761,
            "dislike_count": 19469,
            "artist": "Ali Gatie"
        },
        {
            "song_id": "PMGY8fLwess",
            "song_name": "James Arthur - Falling Like The Stars",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/PMGY8fLwess/maxresdefault.webp"
            },
            "duration": 255,
            "like_count": 532985,
            "dislike_count": 7929,
            "artist": "James Arthur"
        },
        {
            "song_id": "4TA_PqIS1WM",
            "song_name": "Dave Thomas Junior - I Can't Make You Love Me",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/4TA_PqIS1WM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBbkMMKSbIog60hGaaEHWE7tohXYw"
            },
            "duration": 331,
            "like_count": 34084,
            "dislike_count": 1245,
            "artist": "Dave Thomas Junior"
        },
        {
            "song_id": "g5xxhaKm1RQ",
            "song_name": "LANY - Malibu Nights (Official Music Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/g5xxhaKm1RQ/maxresdefault.webp?v=5bc4cff9"
            },
            "duration": 278,
            "like_count": 374199,
            "dislike_count": 4157,
            "artist": "LANY"
        },
        {
            "song_id": "hL_JUT7sWMc",
            "song_name": "Jeremy Zucker & Chelsea Cutler - this is how you fall in love (Live on The Today Show)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/hL_JUT7sWMc/maxresdefault.jpg"
            },
            "duration": 186,
            "like_count": 47977,
            "dislike_count": 113,
            "artist": "Jeremy Zucker, Chelsea Cutler"
        },
        {
            "song_id": "j6Keg3XKKjM",
            "song_name": "Hollow Coves - These Memories (Official Music Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/j6Keg3XKKjM/maxresdefault.webp"
            },
            "duration": 313,
            "like_count": 218955,
            "dislike_count": 2370,
            "artist": "Hollow Coves"
        },
        {
            "song_id": "nORMdEUWaMg",
            "song_name": "Peter Manos - In My Head (Official Music Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/nORMdEUWaMg/maxresdefault.webp"
            },
            "duration": 206,
            "like_count": 56413,
            "dislike_count": 820,
            "artist": "Peter Manos"
        },
        {
            "song_id": "dTxTUDL4A-E",
            "song_name": "#1 Sad Song Playlist (Lyrics Video) Love Is Gone, The One That Got Away, You Broke Me First...etc",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/dTxTUDL4A-E/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAb1V9ARR11XxLU4EqZjku03vI6OA"
            },
            "duration": 925,
            "like_count": 364804,
            "dislike_count": 4279,
            "artist": "Lirikyu"
        },
        {
            "song_id": "UjnDpcgJXvA",
            "song_name": "Five Feet Apart - Don't Give Up On Me",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/UjnDpcgJXvA/maxresdefault.webp"
            },
            "duration": 200,
            "like_count": 999008,
            "dislike_count": 5182,
            "artist": "Andy Grammer"
        },
        {
            "song_id": "RHUUy3acptk",
            "song_name": "At My Worst",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/RHUUy3acptk/maxresdefault.webp"
            },
            "duration": 170,
            "like_count": 170863,
            "dislike_count": 6353,
            "artist": "Pink Sweat$"
        },
        {
            "song_id": "ldElCttO1kk",
            "song_name": "PUBLIC - Make You Mine (Put Your Hand in Mine) [The Sequel]",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/ldElCttO1kk/maxresdefault.jpg?v=5e41ec37"
            },
            "duration": 318,
            "like_count": 308773,
            "dislike_count": 4263,
            "artist": "PUBLIC, Danielle Bradbery"
        },
        {
            "song_id": "0yW7w8F2TVA",
            "song_name": "James Arthur - Say You Won't Let Go",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/0yW7w8F2TVA/maxresdefault.webp"
            },
            "duration": 211,
            "like_count": 6698844,
            "dislike_count": 170944,
            "artist": "James Arthur"
        },
        {
            "song_id": "Jtauh8GcxBY",
            "song_name": "Lewis Capaldi - Before You Go (Official Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/Jtauh8GcxBY/maxresdefault.webp?v=5e4ba761"
            },
            "duration": 246,
            "like_count": 2451359,
            "dislike_count": 35467,
            "artist": "Lewis Capaldi"
        },
        {
            "song_id": "wWYr-35O0Ww",
            "song_name": "Chelsea Cutler - Crazier Things (with Noah Kahan) (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/wWYr-35O0Ww/maxresdefault.webp"
            },
            "duration": 265,
            "like_count": 37198,
            "dislike_count": 331,
            "artist": "Chelsea Cutler, Noah Kahan"
        },
        {
            "song_id": "r1Fx0tqK5Z4",
            "song_name": "Sasha Sloan - Older (Lyric Video)",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/r1Fx0tqK5Z4/maxresdefault.jpg"
            },
            "duration": 192,
            "like_count": 792256,
            "dislike_count": 6314,
            "artist": "Sasha Sloan"
        },
        {
            "song_id": "mw5VIEIvuMI",
            "song_name": "Naomi Scott - Speechless (from Aladdin) (Official Video)",
            "artist": "Naomi Scott",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/mw5VIEIvuMI/maxresdefault.jpg"
            },
            "duration": 206,
            "like_count": 2987316,
            "dislike_count": 46676
        },
        {
            "song_id": "fJ9rUzIMcZQ",
            "song_name": "Queen \u2013 Bohemian Rhapsody (Official Video Remastered)",
            "artist": "Queen",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/fJ9rUzIMcZQ/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLC7tkjMN8pT-zh4iBw5n9zg11OMFQ"
            },
            "duration": 359,
            "like_count": 8881290,
            "dislike_count": 282733
        },
        {
            "song_id": "7F37r50VUTQ",
            "song_name": "ZAYN, Taylor Swift - I Don\u2019t Wanna Live Forever (Fifty Shades Darker)",
            "artist": "ZAYN, Taylor Swift",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/7F37r50VUTQ/maxresdefault.jpg"
            },
            "duration": 257,
            "like_count": 4404412,
            "dislike_count": 187334
        },
        {
            "song_id": "RBumgq5yVrA",
            "song_name": "Passenger | Let Her Go (Official Video)",
            "artist": "null",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/RBumgq5yVrA/maxresdefault.webp"
            },
            "duration": 254,
            "like_count": 12479445,
            "dislike_count": 372613
        },
        {
            "song_id": "LjhCEhWiKXk",
            "song_name": "Bruno Mars - Just The Way You Are (Official Music Video)",
            "artist": "Bruno Mars",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/LjhCEhWiKXk/maxresdefault.jpg"
            },
            "duration": 237,
            "like_count": 6242074,
            "dislike_count": 223554
        },
        {
            "song_id": "87gWaABqGYs",
            "song_name": "Ed Sheeran - Galway Girl [Official Music Video]",
            "artist": "Ed Sheeran",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/87gWaABqGYs/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCONKAXv8zxOC2s_oi9xFxc3Empfw"
            },
            "duration": 199,
            "like_count": 3485451,
            "dislike_count": 103243
        },
        {
            "song_id": "09R8_2nJtjg",
            "song_name": "Maroon 5 - Sugar (Official Music Video)",
            "artist": "Maroon 5",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/09R8_2nJtjg/maxresdefault.jpg"
            },
            "duration": 301,
            "like_count": 13167825,
            "dislike_count": 550226
        },
        {
            "song_id": "-FyjEnoIgTM",
            "song_name": "Bruno Mars - Versace on the Floor (Official Music Video)",
            "artist": "Bruno Mars",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/-FyjEnoIgTM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBhiCJXSUBh8eXFXuJbhIrPawSCOg"
            },
            "duration": 337,
            "like_count": 2217446,
            "dislike_count": 80349
        },
        {
            "song_id": "RB-RcX5DS5A",
            "song_name": "Coldplay - The Scientist (Official Video)",
            "artist": "Coldplay",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/RB-RcX5DS5A/maxresdefault.jpg"
            },
            "duration": 265,
            "like_count": 4371134,
            "dislike_count": 118743
        },
        {
            "song_id": "HgzGwKwLmgM",
            "song_name": "Queen - Don't Stop Me Now (Official Video)",
            "artist": "Queen",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/HgzGwKwLmgM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAM8UqmFmnK5DyvGevPbHHZU_blAQ"
            },
            "duration": 217,
            "like_count": 4181569,
            "dislike_count": 91741
        },
        {
            "song_id": "rY0WxgSXdEE",
            "song_name": "Queen - Another One Bites the Dust (Official Video)",
            "artist": "Queen",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/rY0WxgSXdEE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCRSNHmUTGk1cvbJVcvtemvleRI4g"
            },
            "duration": 223,
            "like_count": 2849969,
            "dislike_count": 66270
        },
        {
            "song_id": "2ZBtPf7FOoM",
            "song_name": "Queen - Killer Queen (Top Of The Pops, 1974)",
            "artist": "Queen",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/2ZBtPf7FOoM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD6hKmjWo6uWkHpe8R3GitMsXQx8w"
            },
            "duration": 192,
            "like_count": 1338233,
            "dislike_count": 20507
        },
        {
            "song_id": "bfigBuN9vVI",
            "song_name": "Name Tag - Nivicious feat. Adam Sjostrand",
            "artist": "Nivicious",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/bfigBuN9vVI/maxresdefault.webp"
            },
            "duration": 196,
            "like_count": 11232,
            "dislike_count": 134
        },
        {
            "song_id": "VsKoOH6DVys",
            "song_name": "Taylor Swift - London Boy (Official Audio)",
            "artist": "Taylor Swift",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/VsKoOH6DVys/maxresdefault.jpg"
            },
            "duration": 191,
            "like_count": 150090,
            "dislike_count": 2131
        },
        {
            "song_id": "MXLydu0Gzdo",
            "song_name": "Phoebe Ryan - Mine (Official Video)",
            "artist": "Phoebe Ryan",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/MXLydu0Gzdo/maxresdefault.webp"
            },
            "duration": 228,
            "like_count": 60780,
            "dislike_count": 562
        },
        {
            "song_id": "jYa1eI1hpDE",
            "song_name": "Taylor Swift - Mean",
            "artist": "Taylor Swift",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/jYa1eI1hpDE/maxresdefault.jpg"
            },
            "duration": 243,
            "like_count": 1104131,
            "dislike_count": 35950
        },
        {
            "song_id": "GTEFSuFfgnU",
            "song_name": "Taylor Swift - Death By A Thousand Cuts (Official Audio)",
            "artist": "Taylor Swift",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/GTEFSuFfgnU/maxresdefault.jpg"
            },
            "duration": 200,
            "like_count": 101605,
            "dislike_count": 1018
        },
        {
            "song_id": "8bKCv1AQvnE",
            "song_name": "Let it Snow | Don't Take The Money",
            "artist": "Bleachers",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/8bKCv1AQvnE/maxresdefault.webp"
            },
            "duration": 216,
            "like_count": 14531,
            "dislike_count": 102
        },
        {
            "song_id": "UjnDpcgJXvA",
            "song_name": "Five Feet Apart - Don't Give Up On Me",
            "artist": "Andy Grammer",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/UjnDpcgJXvA/maxresdefault.webp"
            },
            "duration": 200,
            "like_count": 997594,
            "dislike_count": 5167
        },
        {
            "song_id": "WXEUvdU1S4c",
            "song_name": "Sometimes feel so happy, sometimes feel so sad / Otis & maeve",
            "artist": "The Velvet Underground",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/WXEUvdU1S4c/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDX1vpl0GM5GtQP0m4W1T0G9iniCw"
            },
            "duration": 231,
            "like_count": 434,
            "dislike_count": 4
        },
        {
            "song_id": "WQq98YPV8yk",
            "song_name": "Ashe - Moral of the Story (Official Audio)",
            "artist": "null",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/WQq98YPV8yk/maxresdefault.jpg"
            },
            "duration": 201,
            "like_count": 1293516,
            "dislike_count": 10898
        },
        {
            "song_id": "YO_nkG-RyY0",
            "song_name": "The Perfect Date | Fann & Dave Aud\u00e9 - Shiny Things",
            "artist": "Fann, Dave Aud\u00e9",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/YO_nkG-RyY0/maxresdefault.webp"
            },
            "duration": 191,
            "like_count": 5450,
            "dislike_count": 43
        },
        {
            "song_id": "BcqxLCWn-CE",
            "song_name": "Lauv - I Like Me Better [Official Video]",
            "artist": "Lauv",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/BcqxLCWn-CE/maxresdefault.webp"
            },
            "duration": 205,
            "like_count": 1600637,
            "dislike_count": 24513
        },
        {
            "song_id": "EgBJmlPo8Xw",
            "song_name": "Billie Eilish - everything i wanted",
            "artist": "Billie Eilish",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/EgBJmlPo8Xw/maxresdefault.jpg"
            },
            "duration": 288,
            "like_count": 4313189,
            "dislike_count": 88209
        },
        {
            "song_id": "AWtzggyXnWg",
            "song_name": "The Girl next door Soundtrack  - This Year's Love - ( David Gray )",
            "artist": "David Gray",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/AWtzggyXnWg/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDUcfdF5UnktWZ9bP08_Wmkip3XDg"
            },
            "duration": 246,
            "like_count": 1315,
            "dislike_count": 27
        },
        {
            "song_id": "h0KkO8N9-U4",
            "song_name": "the girl next door",
            "artist": "Hoobastank",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/h0KkO8N9-U4/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAcWJbQ0EOxKJWIdnmFZzaGhalxDw"
            },
            "duration": 235,
            "like_count": 306,
            "dislike_count": 16
        },
        {
            "song_id": "a2VUbOCbNM0",
            "song_name": "Be Like That (Girl Next Door)",
            "artist": "3 Doors Down",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/a2VUbOCbNM0/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCPRK5zIXhb3FGaHtK_Sg3SvyzSeg"
            },
            "duration": 240,
            "like_count": 448,
            "dislike_count": 10
        },
        {
            "song_id": "FMSU4QDbdew",
            "song_name": "Elliott Smith - Angeles",
            "artist": "Elliott Smith",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/FMSU4QDbdew/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLANNGG0f-PbClldCMFvCOg1GUHZVQ"
            },
            "duration": 175,
            "like_count": 29236,
            "dislike_count": 296
        },
        {
            "song_id": "rlrm9gzwAi0",
            "song_name": "Maybe You're Gone by Binocular",
            "artist": "null",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/rlrm9gzwAi0/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDr8E_WwVKslkLGEASsUrVo3MuqbA"
            },
            "duration": 158,
            "like_count": 579,
            "dislike_count": 14
        },
        {
            "song_id": "gegzDLWJtmU",
            "song_name": "Hannah + Clay {Their Story}  | 13 Reasons Why",
            "artist": "null",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/gegzDLWJtmU/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDsKVgyoSTxTDi15R8ov-u6k1Jrvw"
            },
            "duration": 486,
            "like_count": 85078,
            "dislike_count": 809
        },
        {
            "song_id": "aLVlS-mHQbw",
            "song_name": "Leaving On A Jet Plane - John Denver (cover) | Rene\u00e9 Dominique",
            "artist": "null",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/aLVlS-mHQbw/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBvzvsuDqbFLkr7_PIligH8K_H27Q"
            },
            "duration": 331,
            "like_count": 111213,
            "dislike_count": 1625
        },
        {
            "song_id": "euHGXlYrLNk",
            "song_name": "Twilight Soundtrack - Flightless bird, American mouth",
            "artist": "Iron & Wine",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/euHGXlYrLNk/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBPGINngWR8eVLPaF1gDmwZUiDXKw"
            },
            "duration": 237,
            "like_count": 144057,
            "dislike_count": 2777
        },
        {
            "song_id": "kql9cw2MtCU",
            "song_name": "Husavik (My Home Town) | Molly Sand\u00e9n - The Real Voice Behind the Song | Eurovision",
            "artist": "null",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/kql9cw2MtCU/maxresdefault.jpg"
            },
            "duration": 218,
            "like_count": 41499,
            "dislike_count": 371
        },
        {
            "song_id": "vLrfjqgLbNU",
            "song_name": "What A Wonderful World.avi",
            "artist": "null",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/vLrfjqgLbNU/maxresdefault.jpg"
            },
            "duration": 149,
            "like_count": 406283,
            "dislike_count": 3325
        },
        {
            "song_id": "hwZNL7QVJjE",
            "song_name": "Ben E. King - Stand By Me",
            "artist": "Ben E. King",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/hwZNL7QVJjE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAh7VLzoT3u6NLa-99LX_s-QaJuuA"
            },
            "duration": 178,
            "like_count": 3477979,
            "dislike_count": 74839
        },
        {
            "song_id": "hwfwqA55w_0",
            "song_name": "Spanish Harlem",
            "artist": "Ben E. King",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/hwfwqA55w_0/maxresdefault.webp"
            },
            "duration": 174,
            "like_count": 4015,
            "dislike_count": 898
        },
        {
            "song_id": "jJPMnTXl63E",
            "song_name": "Powfu - death bed (coffee for your head) (Official Video) ft. beabadoobee",
            "artist": "Powfu, beabadoobee",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/jJPMnTXl63E/maxresdefault.jpg"
            },
            "duration": 174,
            "like_count": 5259487,
            "dislike_count": 71242
        },
        {
            "song_id": "nLnp0tpZ0ok",
            "song_name": "PUBLIC - Make You Mine (Put Your Hand in Mine) [Official Video]",
            "artist": "PUBLIC, Danielle Bradbery",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/nLnp0tpZ0ok/maxresdefault.jpg?v=5da3bc69"
            },
            "duration": 236,
            "like_count": 2000256,
            "dislike_count": 18561
        },
        {
            "song_id": "ldElCttO1kk",
            "song_name": "PUBLIC - Make You Mine (Put Your Hand in Mine) [The Sequel]",
            "artist": "PUBLIC, Danielle Bradbery",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/ldElCttO1kk/maxresdefault.jpg?v=5e41ec37"
            },
            "duration": 318,
            "like_count": 308452,
            "dislike_count": 4260
        },
        {
            "song_id": "VUCuoxOUD6U",
            "song_name": "Electric Love - B\u00d8RNS (Lyrics) \ud83c\udfb5",
            "artist": "null",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/VUCuoxOUD6U/maxresdefault.webp"
            },
            "duration": 252,
            "like_count": 583091,
            "dislike_count": 7404
        },
        {
            "song_id": "89degLrNZM8",
            "song_name": "Surf Mesa - ily (i love you baby) ft. Emilee",
            "artist": "Surf Mesa",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/89degLrNZM8/maxresdefault.jpg"
            },
            "duration": 177,
            "like_count": 961748,
            "dislike_count": 15635
        },
        {
            "song_id": "eIc4mqyN1Q8",
            "song_name": "Trevor Daniel - Falling (Lyrics)",
            "artist": "Trevor Daniel",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/eIc4mqyN1Q8/maxresdefault.webp"
            },
            "duration": 159,
            "like_count": 4868915,
            "dislike_count": 64303
        },
        {
            "song_id": "m7Bc3pLyij0",
            "song_name": "Marshmello ft. Bastille - Happier (Official Music Video)",
            "artist": "Marshmello, Bastille",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/m7Bc3pLyij0/maxresdefault.webp?v=5c5c992f"
            },
            "duration": 233,
            "like_count": 11164418,
            "dislike_count": 304798
        },
        {
            "song_id": "9P16xvwMQ5A",
            "song_name": "Pink Floyd - Wish You Were Here (Eternal Sunshine of the Spotless Mind) [HD]",
            "artist": "Pink Floyd",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/9P16xvwMQ5A/maxresdefault.webp"
            },
            "duration": 303,
            "like_count": 309467,
            "dislike_count": 4818
        },
        {
            "song_id": "50VNCymT-Cs",
            "song_name": "Alec Benjamin - Let Me Down Slowly [Official Music Video]",
            "artist": "Alec Benjamin",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/50VNCymT-Cs/maxresdefault.webp"
            },
            "duration": 177,
            "like_count": 3871809,
            "dislike_count": 46914
        },
        {
            "song_id": "Zzylc-7PwQ4",
            "song_name": "SHAED x ZAYN - Trampoline (Official Lyric Video)",
            "artist": "SHAED, ZAYN",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/Zzylc-7PwQ4/maxresdefault.webp"
            },
            "duration": 187,
            "like_count": 551437,
            "dislike_count": 5386
        },
        {
            "song_id": "UmQjdvSH5qk",
            "song_name": "aiivawn \u2013 can't take my eyes off you (lofi edit) ft. CRAYMER [official audio]",
            "artist": "null",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/UmQjdvSH5qk/maxresdefault.webp"
            },
            "duration": 241,
            "like_count": 82891,
            "dislike_count": 670
        },
        {
            "song_id": "SJOgTMP8cs4",
            "song_name": "The Chainsmokers - Hope ft. Winona Oak (Lyric Video)",
            "artist": "The Chainsmokers",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/SJOgTMP8cs4/maxresdefault.webp"
            },
            "duration": 193,
            "like_count": 891583,
            "dislike_count": 22237
        },
        {
            "song_id": "mj0XInqZMHY",
            "song_name": "Ed Sheeran - Beautiful People (feat. Khalid) [Official Music Video]",
            "artist": "Ed Sheeran",
            "image": {
                "image_id": "3",
                "resolution": "336x188",
                "image_url": "https://i.ytimg.com/vi/mj0XInqZMHY/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCQtUMRWGLIWuspGbR_q7fV051CdQ"
            },
            "duration": 228,
            "like_count": 2465488,
            "dislike_count": 68057
        },
        {
            "song_id": "pvPsJFRGleA",
            "song_name": "Justin Bieber - Holy ft. Chance The Rapper",
            "artist": "Justin Bieber",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/pvPsJFRGleA/maxresdefault.jpg?v=5f638ee0"
            },
            "duration": 329,
            "like_count": 3588357,
            "dislike_count": 96144
        },
        {
            "song_id": "tD4HCZe-tew",
            "song_name": "Zara Larsson - Lush Life",
            "artist": "Zara Larsson",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/tD4HCZe-tew/maxresdefault.webp"
            },
            "duration": 202,
            "like_count": 4099042,
            "dislike_count": 120289
        },
        {
            "song_id": "r65ASraC7nM",
            "song_name": "Loving Caliber feat. Lauren Dunn - Invested",
            "artist": "Loving Caliber",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/r65ASraC7nM/maxresdefault.webp"
            },
            "duration": 217,
            "like_count": 1437,
            "dislike_count": 26
        },
        {
            "song_id": "6qkgVgjN188",
            "song_name": "Jeremy Zucker & Chelsea Cutler - this is how you fall in love (Official Music Video)",
            "artist": "Jeremy Zucker, Chelsea Cutler",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/6qkgVgjN188/maxresdefault.jpg?v=5fff26e4"
            },
            "duration": 177,
            "like_count": 107537,
            "dislike_count": 560
        },
        {
            "song_id": "Yo0RIfqPiUw",
            "song_name": "ScoopWhoop: 60 Years Of Bollywood Part II | SW Cafe |  Session V",
            "artist": "Shaan, Kavita Krishanamurty",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/Yo0RIfqPiUw/maxresdefault.webp"
            },
            "duration": 487,
            "like_count": 96043,
            "dislike_count": 1476
        },
        {
            "song_id": "yYchF3OLkm4",
            "song_name": "Astrid S - It\u00b4s Ok If You Forget Me (Official Lyric Video)",
            "artist": "Astrid S",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/yYchF3OLkm4/maxresdefault.jpg"
            },
            "duration": 208,
            "like_count": 426975,
            "dislike_count": 2091
        },
        {
            "song_id": "9Sc-ir2UwGU",
            "song_name": "Kygo - Firestone ft. Conrad Sewell (Official Video)",
            "artist": "Kygo",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/9Sc-ir2UwGU/maxresdefault.webp"
            },
            "duration": 222,
            "like_count": 3124819,
            "dislike_count": 87340
        },
        {
            "song_id": "PIh2xe4jnpk",
            "song_name": "MAGIC! - Rude (Official Music Video)",
            "artist": "MAGIC!",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/PIh2xe4jnpk/maxresdefault.jpg"
            },
            "duration": 225,
            "like_count": 8664782,
            "dislike_count": 314147
        },
        {
            "song_id": "ZPMWJ7DpzoY",
            "song_name": "Rudimental - Come Over (feat. Anne-Marie) [Official Acoustic]",
            "artist": "Rudimental",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/ZPMWJ7DpzoY/maxresdefault.webp"
            },
            "duration": 195,
            "like_count": 203129,
            "dislike_count": 1703
        },
        {
            "song_id": "F8Jxo15Vfic",
            "song_name": "All Too Well",
            "artist": "Taylor Swift",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/F8Jxo15Vfic/maxresdefault.webp"
            },
            "duration": 329,
            "like_count": 44561,
            "dislike_count": 676
        },
        {
            "song_id": "NF00IaYXZ5w",
            "song_name": "Sunflower - Movie Version",
            "artist": "Shannon Purser",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/NF00IaYXZ5w/maxresdefault.webp"
            },
            "duration": 108,
            "like_count": 629,
            "dislike_count": 23
        },
        {
            "song_id": "06k5XN78OP0",
            "song_name": "Jeremy Zucker, Chelsea Cutler - you were good to me (Official Video)",
            "artist": "Jeremy Zucker, Chelsea Cutler",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi_webp/06k5XN78OP0/maxresdefault.webp"
            },
            "duration": 221,
            "like_count": 252082,
            "dislike_count": 1859
        },
        {
            "song_id": "PAXESZ11f3g",
            "song_name": "Sasha Sloan - Older (Acoustic Video)",
            "artist": "Sasha Sloan",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/PAXESZ11f3g/maxresdefault.jpg"
            },
            "duration": 212,
            "like_count": 42385,
            "dislike_count": 258
        },
        {
            "song_id": "lMk3WMnUZ1s",
            "song_name": "sports - you are the right one (legendado)",
            "artist": "Sports",
            "image": {
                "image_id": "4",
                "resolution": "1920x1080",
                "image_url": "https://i.ytimg.com/vi/lMk3WMnUZ1s/maxresdefault.jpg"
            },
            "duration": 175,
            "like_count": 311731,
            "dislike_count": 1092
        }
    ]
}

def load_random_song():
    # with open('/audiocave-backend/music_room/ytd_player.json', 'r') as f:
    length_ = len(random_data['objects'])
    data = random_data['objects']
    # ss = random.choice(data)
    dd = random.randint(0, length_)
    return data[dd]["song_id"]
    # return ss["song_id"]
