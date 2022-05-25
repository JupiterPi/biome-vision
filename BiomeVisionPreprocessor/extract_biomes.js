// this script can be copy-pasted to Chrome Dev Tools to extract all biome ids from https://minecraft.fandom.com/wiki/Biome/ID
// first, the table element that contains the biome ids has to be manually changed to have the id "mytable" assigned

mytable = document.getElementById("mytable");
mytrs = mytable.getElementsByTagName("tr");
for (let tr of mytrs) {
    console.log(tr.getElementsByTagName("td")[1].getElementsByTagName("code")[0].innerText);
}