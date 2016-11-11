var res = [];
var offset = 0;
while (offset < 1603) {
    res = res + API.wall.get({
        "domain": "kamen_v_lesu",
        "offset": offset,
        "count": 100,
        "filter": "owner"
    }).items;
    offset = offset + 100;
}
return res;