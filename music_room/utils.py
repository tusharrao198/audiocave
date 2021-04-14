import random
import json

random_data = {
    "objects": [
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
    data = random_data['objects']
    ss = random.choice(data)
    return ss["song_id"]
