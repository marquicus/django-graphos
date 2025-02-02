from .models import Account


DB_HOST = ["localhost"]
DB_PORT = 27017


def get_db(db_name):
    import pymongo
    DB_HOST = ["localhost"]
    DB_PORT = 27017
    db = pymongo.Connection(DB_HOST, DB_PORT)[db_name]
    return db


def get_mongo_cursor(db_name, collection_name, max_docs=100):
    import pymongo
    db = pymongo.Connection(host=DB_HOST,
                            port=DB_PORT)[db_name]
    collection = db[collection_name]
    cursor = collection.find()
    count = cursor.count
    if callable(count):
        count = count()
    if count >= max_docs:
        cursor = cursor[0:max_docs]
    return cursor


data = [
       ['Year', 'Sales', 'Expenses', 'Items Sold', 'Net Profit'],
       ['2004', 1000, 400, 100, 600],
       ['2005', 1170, 460, 120, 710],
       ['2006', 660, 1120, 50, -460],
       ['2007', 1030, 540, 100, 490],
]

candlestick_data = [
    ['Mon', 20, 28, 38, 45],
    ['Tue', 31, 38, 55, 66],
    ['Wed', 50, 55, 77, 80],
    ['Thu', 77, 77, 66, 50],
    ['Fri', 68, 66, 22, 15]
]

# TODO: Come up with a better example
scatter_multi_series_data = [
    ['state', 'country', 'Rainfall', 'Precipitation'],
    ['Uttar Pradesh', 'India', 1, 2],
    ['Bihar', 'India', 2, 3],
    ['Telangana', 'India', 5, 7],
    ['Lahore', 'Pakistan', 9, 8],
    ['Hyderabad', 'Pakistan', 8, 7],
    ['Lahore', 'Pakistan', 3, 11]
]

# TODO: Come up with a better example
scatter_single_series_data = [
    ['Leader', 'Rainfall', 'Precipitation'],
    ['Trump', 1, 2],
    ['Clinton', 2, 3],
    ['Trumps', 5, 7],
    ['George', 6, 9],
    ['Alex', 7, 4],
    ['Donald', 7, 8],
]

treemap_data = [
    ['Location', 'Parent', 'Market trade volume (size)', 'Market increase/decrease (color)'],
    ['Global', None, 0, 0],
    ['America', 'Global', 0, 0],
    ['Europe', 'Global', 0, 0],
    ['Asia', 'Global', 0, 0],
    ['Australia', 'Global', 0, 0],
    ['Africa', 'Global', 0, 0],
    ['Brazil', 'America', 11, 10],
    ['USA', 'America', 52, 31],
    ['Mexico', 'America', 24, 12],
    ['Canada', 'America', 16, -23],
    ['France', 'Europe', 42, -11],
    ['Germany', 'Europe', 31, -2],
    ['Sweden', 'Europe', 22, -13],
    ['Italy', 'Europe', 17, 4],
    ['UK', 'Europe', 21, -5],
    ['China', 'Asia', 36, 4],
    ['Japan', 'Asia', 20, -12],
    ['India', 'Asia', 40, 63],
    ['Laos', 'Asia', 4, 34],
    ['Mongolia', 'Asia', 1, -5],
    ['Israel', 'Asia', 12, 24],
    ['Iran', 'Asia', 18, 13],
    ['Pakistan', 'Asia', 11, -52],
    ['Egypt', 'Africa', 21, 0],
    ['S. Africa', 'Africa', 30, 43],
    ['Sudan', 'Africa', 12, 2],
    ['Congo', 'Africa', 10, 12],
    ['Zaire', 'Africa', 8, 10]
]


# map_data = [
#     ['Country', 'Value'],
#     ['fo', 0],
#     ['um', 1],
#     ['us', 2],
#     ['jp', 3],
#     ['sc', 4],
#     ['in', 5],
#     ['fr', 6],
#     ['fm', 7],
#     ['cn', 8],
#     ['pt', 9],
#     ['sw', 10],
#     ['sh', 11],
#     ['br', 12],
#     ['ki', 13],
#     ['ph', 14],
#     ['mx', 15],
#     ['es', 16],
#     ['bu', 17],
#     ['mv', 18],
#     ['sp', 19],
#     ['gb', 20],
#     ['gr', 21],
#     ['as', 22],
#     ['dk', 23],
#     ['gl', 24],
#     ['gu', 25],
#     ['mp', 26],
#     ['pr', 27],
#     ['vi', 28],
#     ['ca', 29],
#     ['st', 30],
#     ['cv', 31],
#     ['dm', 32],
#     ['nl', 33],
#     ['jm', 34],
#     ['ws', 35],
#     ['om', 36],
#     ['vc', 37],
#     ['tr', 38],
#     ['bd', 39],
#     ['lc', 40],
#     ['nr', 41],
#     ['no', 42],
#     ['kn', 43],
#     ['bh', 44],
#     ['to', 45],
#     ['fi', 46],
#     ['id', 47],
#     ['mu', 48],
#     ['se', 49],
#     ['tt', 50],
#     ['my', 51],
#     ['pa', 52],
#     ['pw', 53],
#     ['tv', 54],
#     ['mh', 55],
#     ['cl', 56],
#     ['th', 57],
#     ['gd', 58],
#     ['ee', 59],
#     ['ad', 60],
#     ['tw', 61],
#     ['bb', 62],
#     ['it', 63],
#     ['mt', 64],
#     ['vu', 65],
#     ['sg', 66],
#     ['cy', 67],
#     ['lk', 68],
#     ['km', 69],
#     ['fj', 70],
#     ['ru', 71],
#     ['va', 72],
#     ['sm', 73],
#     ['kz', 74],
#     ['az', 75],
#     ['tj', 76],
#     ['ls', 77],
#     ['uz', 78],
#     ['ma', 79],
#     ['co', 80],
#     ['tl', 81],
#     ['tz', 82],
#     ['ar', 83],
#     ['sa', 84],
#     ['pk', 85],
#     ['ye', 86],
#     ['ae', 87],
#     ['ke', 88],
#     ['pe', 89],
#     ['do', 90],
#     ['ht', 91],
#     ['pg', 92],
#     ['ao', 93],
#     ['kh', 94],
#     ['vn', 95],
#     ['mz', 96],
#     ['cr', 97],
#     ['bj', 98],
#     ['ng', 99],
#     ['ir', 100],
#     ['sv', 101],
#     ['sl', 102],
#     ['gw', 103],
#     ['hr', 104],
#     ['bz', 105],
#     ['za', 106],
#     ['cf', 107],
#     ['sd', 108],
#     ['cd', 109],
#     ['kw', 110],
#     ['de', 111],
#     ['be', 112],
#     ['ie', 113],
#     ['kp', 114],
#     ['kr', 115],
#     ['gy', 116],
#     ['hn', 117],
#     ['mm', 118],
#     ['ga', 119],
#     ['gq', 120],
#     ['ni', 121],
#     ['lv', 122],
#     ['ug', 123],
#     ['mw', 124],
#     ['am', 125],
#     ['sx', 126],
#     ['tm', 127],
#     ['zm', 128],
#     ['nc', 129],
#     ['mr', 130],
#     ['dz', 131],
#     ['lt', 132],
#     ['et', 133],
#     ['er', 134],
#     ['gh', 135],
#     ['si', 136],
#     ['gt', 137],
#     ['ba', 138],
#     ['jo', 139],
#     ['sy', 140],
#     ['mc', 141],
#     ['al', 142],
#     ['uy', 143],
#     ['cnm', 144],
#     ['mn', 145],
#     ['rw', 146],
#     ['so', 147],
#     ['bo', 148],
#     ['cm', 149],
#     ['cg', 150],
#     ['eh', 151],
#     ['rs', 152],
#     ['me', 153],
#     ['tg', 154],
#     ['la', 155],
#     ['af', 156],
#     ['ua', 157],
#     ['sk', 158],
#     ['jk', 159],
#     ['bg', 160],
#     ['qa', 161],
#     ['li', 162],
#     ['at', 163],
#     ['sz', 164],
#     ['hu', 165],
#     ['ro', 166],
#     ['ne', 167],
#     ['lu', 168],
#     ['ad', 169],
#     ['ci', 170],
#     ['lr', 171],
#     ['bn', 172],
#     ['iq', 173],
#     ['ge', 174],
#     ['gm', 175],
#     ['ch', 176],
#     ['td', 177],
#     ['kv', 178],
#     ['lb', 179],
#     ['dj', 180],
#     ['bi', 181],
#     ['sr', 182],
#     ['il', 183],
#     ['ml', 184],
#     ['sn', 185],
#     ['gn', 186],
#     ['zw', 187],
#     ['pl', 188],
#     ['mk', 189],
#     ['py', 190],
#     ['by', 191],
#     ['ca', 192],
#     ['bf', 193],
#     ['na', 194],
#     ['ly', 195],
#     ['tn', 196],
#     ['bt', 197],
#     ['md', 198],
#     ['ss', 199],
#     ['bw', 200],
#     ['bs', 201],
#     ['nz', 202],
#     ['cu', 203],
#     ['ec', 204],
#     ['au', 205],
#     ['ve', 206],
#     ['sb', 207],
#     ['mg', 208],
#     ['is', 209],
#     ['eg', 210],
#     ['kg', 211],
#     ['np', 212]
# ]


map_data = [
    ['Country', 'Value'],
    ['fo', 0],
    ['um', 1],
    ['us', 2],
    ['jp', 3],
    ['sc', 4],
    ['in', 5],
    ['fr', 6],
    ['fm', 7],
    ['cn', 8],
    ['pt', 9],
    ['sw', 10],
    ['sh', 11],
    ['br', 12],
    ['ki', 13],
    ['ph', 14],
    ['mx', 15],
    ['es', 16],
    ['bu', 17],
    ['mv', 18],
    ['sp', 19],
    ['gb', 20],
    ['gr', 21],
    ['as', 22],
    ['dk', 23],
    ['gl', 24],
    ['gu', 25],
    ['mp', 26],
    ['pr', 27],
    ['vi', 28],
    ['ca', 29],
    ['st', 30],
    ['cv', 31],
    ['dm', 32],
    ['nl', 33],
    ['jm', 34],
    ['ws', 35],
    ['om', 36],
    ['vc', 37],
    ['tr', 38],
    ['bd', 39],
    ['lc', 40],
    ['nr', 41],
    ['no', 42],
    ['kn', 43],
    ['bh', 44],
    ['to', 45],
    ['fi', 46],
    ['id', 47],
    ['mu', 48],
    ['se', 49],
    ['tt', 50],
    ['my', 51],
    ['pa', 52],
    ['pw', 53],
    ['tv', 54],
    ['mh', 55],
    ['cl', 56],
    ['th', 57],
    ['gd', 58],
    ['ee', 59],
    ['ad', 60],
    ['tw', 61],
    ['bb', 62],
    ['it', 63],
    ['mt', 64],
    ['vu', 65],
    ['sg', 66],
    ['cy', 67],
    ['lk', 68],
    ['km', 69],
    ['fj', 70],
    ['ru', 71],
    ['va', 72],
    ['sm', 73],
    ['kz', 74],
    ['az', 75],
    ['tj', 76],
    ['ls', 77],
    ['uz', 78],
    ['ma', 79],
    ['co', 80],
    ['tl', 81],
    ['tz', 82],
    ['ar', 83],
    ['sa', 84],
    ['pk', 85],
    ['ye', 86],
    ['ae', 87],
    ['ke', 88],
    ['pe', 89],
    ['do', 90],
    ['ht', 91],
    ['pg', 92],
    ['ao', 93],
    ['kh', 94],
    ['vn', 95],
    ['mz', 96],
    ['cr', 97],
    ['bj', 98],
    ['ng', 99]
]


map_data_us_multi_series_lat_lon = [
    ['Latitude', 'Longitude', 'Winner', 'Seats'],
    [32.380120, -86.300629, 'Trump', 10],
    [58.299740, -134.406794, 'Trump', 10],
    [33.448260, -112.075774, 'Trump', 10],
    [34.748655, -92.274494, 'Clinton', 20],
    [38.579065, -121.491014, 'Clinton', 20],
]


map_data_us_multi_series = [
    ['State', 'Winner', 'Seats'],
    ['us-nj', 'Trump', 10],
    ['us-ri', 'Trump', 10],
    ['us-ma', 'Trump', 10],
    ['us-ct', 'Clinton', 20],
    ['us-md', 'Clinton', 20],
    ['us-ny', 'Clinton', 20],
    ['us-de', 'Trump', 20],
    ['us-fl', 'Trump', 20],
    ['us-oh', 'Trump', 20],
    ['us-pa', 'Trump', 20],
    ['us-li', 'Trump', 20],
    ['us-ca', 'Trump', 20],
    ['us-hi', 'Trump', 20],
    ['us-va', 'Trump', 31],
    ['us-mi', 'Trump', 31],
    ['us-in', 'Trump', 31],
    ['us-nc', 'Trump', 31],
    ['us-ga', 'Trump', 31],
    ['us-tn', 'Trump', 31],
    ['us-nh', 'Trump', 31],
    ['us-sc', 'Trump', 31],
    ['us-la', 'Trump', 31],
    ['us-ky', 'Trump', 31],
    ['us-wi', 'Trump', 12],
    ['us-wa', 'Trump', 12],
    ['us-al', 'Clinton', 12],
    ['us-mo', 'Clinton', 12],
    ['us-tx', 'Clinton', 45],
    ['us-wv', 'Clinton', 45],
]


map_data_us_lat_lon = [
    ['Latitude', 'Longitude', 'Population'],
    [32.380120, -86.300629, 900],
    [58.299740, -134.406794, 387],
    [33.448260, -112.075774, 313],
]
map_data_india_lat_lon = [
    ['Latitude', 'Longitude', 'Population'],
    [25.4851484, 83.2104426, 900],
    [27.7126407, 78.7391187, 387],
    [28.2699017, 79.1604971, 313],
]


map_data_us = [
    ['State', 'Population'],
    ['us-nj', 438],
    ['us-ri', 387],
    ['us-ma', 313],
    ['us-ct', 271],
    ['us-md', 209],
    ['us-ny', 195],
    ['us-de', 155],
    ['us-fl', 114],
    ['us-oh', 107],
    ['us-pa', 106],
    ['us-li', 86],
    ['us-ca', 84],
    ['us-hi', 73],
    ['us-va', 69],
    ['us-mi', 68],
    ['us-in', 65],
    ['us-nc', 64],
    ['us-ga', 55],
    ['us-tn', 53],
    ['us-nh', 53],
    ['us-sc', 51],
    ['us-la', 40],
    ['us-ky', 39],
    ['us-wi', 38],
    ['us-wa', 34],
    ['us-al', 34],
    ['us-mo', 31],
    ['us-tx', 31],
    ['us-wv', 29],
    ['us-vt', 25],
    ['us-mn', 24],
    ['us-ms', 23],
    ['us-ia', 20],
    ['us-ar', 20],
    ['us-ok', 19],
    ['us-az', 17],
    ['us-co', 16],
    ['us-me', 16],
    ['us-or', 14],
    ['us-ks', 13],
    ['us-ut', 11],
    ['us-ne', 9],
    ['us-nv', 7],
    ['us-id', 6],
    ['us-nm', 6],
    ['us-sd', 4],
    ['us-nd', 4],
    ['us-mt', 2],
    ['us-wy', 2],
    ['us-ak', 1],
]

map_data_us_point = [
    ['Lat', 'Lon', 'Name', 'Date'],
    [46.8797, -110.3626, 'trump', '25th February'],
    [41.4925, -99.9018, 'trump', '26th February'],
    [45.4925, -89.9018, 'trump', '27th February'],
    [32.1656, -82.9001, 'clinton', '25th February'],
    [33.1656, -81.9001, 'clinton', '26th February'],
]


mongo_series_object_1 = [
    [440, 39],
    [488, 29.25],
    [536, 28],
    [584, 29],
    [632, 33.25],
    [728, 28.5],
    [776, 33.25],
    [824, 28.5],
    [872, 31],
    [920, 30.75],
    [968, 26.25]
]

mongo_series_object_2 = [
    [400, 4],
    [488, 0],
    [536, 20],
    [584, 8],
    [632, 2],
    [680, 36],
    [728, 0],
    [776, 0],
    [824, 0],
    [872, 4],
    [920, 1],
    [968, 0]
]

mongo_data = [{'data': mongo_series_object_1, 'label': 'hours'},
              {'data': mongo_series_object_2, 'label': 'hours'}]


def create_demo_accounts():
    Account.objects.all().delete()
    # Create some rows
    Account.objects.create(year="2004", sales=1000,
                           expenses=400, ceo="Welch")
    Account.objects.create(year="2005", sales=1170,
                           expenses=460, ceo="Jobs")
    Account.objects.create(year="2006", sales=660,
                           expenses=1120, ceo="Page")
    Account.objects.create(year="2007", sales=1030,
                           expenses=540, ceo="Welch")
    Account.objects.create(year="2008", sales=2030,
                           expenses=1540, ceo="Zuck")
    Account.objects.create(year="2009", sales=2230,
                           expenses=1840, ceo="Cook")


def create_demo_mongo():
    accounts = get_db("accounts")
    docs = accounts.docs
    docs.drop()

    docs = accounts.docs
    header = data[0]
    data_only = data[1:]
    for row in data_only:
        docs.insert(dict(zip(header, row)))


heatmap_data = [
    ['Name', 'Yash', 'Akshar', 'Ashok', 'Shabda'],
    ['Uttar Pradesh', 1000, 2000, 3000, 4000],
    ['Bihar', 2000, 5000, 8000, 9800],
    ['Hyderabad', 10000, 9855, 6000, 2000],
    ['Banglore', 98652, 78563, 8522, 2000],
    ['Chennai', 98745, 8563, 5236, 2000],
    ['Vizag', 9875, 7000, 966, 2300],
    ['Maharashtra', 9000, 16789, 9087, 6789],
    ['Punjab', 3467, 8900, 5670, 9900]
]

funnel_data = [
    ['Unique users', 'Counts'],
    ['Website visits', 654],
    ['Downloads', 4064],
    ['Requested price list', 1987],
    ['Invoice sent', 976],
    ['Finalized', 846]
]


treemap_data_highcharts = [
    ["Continent", "Country", "Cause", "Death Rate"],
    ["Asia", "India", "Cardiovascular Disease", 10],
    ["Asia", "India", "Road Accident", 5],
    ["Asia", "India", "Cancer", 3],
    ["Asia", "China", "Cardiovascular Disease", 9],
    ["Asia", "China", "Road Accident", 6],
    ["Asia", "China", "Cancer", 1],
    ["South Ameria", "Brazil", "Cardiovascular Disease", 11],
    ["South Ameria", "Brazil", "Road Accident", 3],
    ["South Ameria", "Brazil", "Cancer", 2],
    ["South Ameria", "Uruguay", "Cardiovascular Disease", 12],
    ["South Ameria", "Uruguay", "Road Accident", 9],
    ["South Ameria", "Uruguay", "Cancer", 8],
    ["Europe", "France", "Cardiovascular Disease", 9],
    ["Europe", "France", "Road Accident", 4],
    ["Europe", "France", "Cancer", 6]
]

piechart_data_highcharts = [
    ["Country", "Cause", "Death Rate"],
    ["India", "Cardiovascular Disease", 10],
    ["India", "Road Accident", 5],
    ["India", "Cancer", 3],
    ["China", "Cardiovascular Disease", 9],
    ["China", "Road Accident", 6],
    ["China", "Cancer", 1],
    ["Brazil", "Cardiovascular Disease", 11],
    ["Brazil", "Road Accident", 3],
    ["Brazil", "Cancer", 2],
    ["Uruguay", "Cardiovascular Disease", 12],
    ["Uruguay", "Road Accident", 9],
    ["Uruguay", "Cancer", 8],
    ["France", "Cardiovascular Disease", 9],
    ["France", "Road Accident", 4],
    ["France", "Cancer", 6]
]

bubble_chart_data_multi = [
    ["Grade", "Country", "Sugar Consumption", "Fat Consumption", "GDP"],
    ["A", "India", 10, 15, 90],
    ["B", "India", 11, 20, 19],
    ["C", "India", 12, 15, 70],
    ["D", "India", 13, 30, 39],
    ["E", "India", 14, 12, 9],
    ["F", "India", 15, 5, 98],
    ["H", "Japan", 18, 60, 110],
    ["I", "Japan", 41, 16, 140],
    ["J", "Japan", 47, 36, 150],
    ["K", "Japan", 61, 56, 70],
    ["L", "Japan", 74, 36, 210],
    ["M", "Japan", 10, 46, 90],
    ["N", "Japan", 30, 26, 100],
    ["O", "China", 14, 18, 100],
    ["A", "China", 9, 17, 10],
    ["B", "China", 51, 67, 200],
    ["C", "China", 12, 27, 160],
    ["D", "China", 42, 67, 86],
    ["E", "China", 30, 97, 20],
    ["F", "China", 16, 67, 90],
    ["L", "USA", 56, 20, 120],
    ["K", "USA", 32, 23, 220],
    ["A", "USA", 15, 85, 320],
    ["S", "USA", 48, 10, 20],
    ["D", "USA", 30, 96, 150],
    ["K", "USA", 14, 22, 160],
    ["P", "USA", 39, 21, 100],
    ["O", "USA", 44, 29, 150]
]


bubble_chart_data_single = [
    ["Country", "Sugar Consumption", "Fat Consumption", "GDP"],
    ["India", 10, 15, 90],
    ["USA", 11, 20, 19],
    ["China", 12, 15, 70],
    ["Japan", 13, 30, 39],
    ["Pakistan", 14, 12, 9],
    ["Srilanka", 15, 5, 98],
    ["Indonesia", 16, 35, 150]
]


chartjs_sample_data = [
    ['Sales', 'Expenses', 'Items Sold', 'Net Profit'],
    [2004, 1000, 400, 100, 600],
    [2005, 1170, 460, 120, 310]]


chartjs_single_series = [
    ['Sales', 'Expenses', 'Items Sold', 'Net Profit'],
    ['First dataset', 1000, 400, 100, 600]
]
