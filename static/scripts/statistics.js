let example = "<button class=\"w3-button w3-block w3-white w3-left-align\" onclick=\"revealOnAccordion('tech')\">Tech ▼</button>"
let examplediv = "<div class=\"w3-hide w3-animate-opacity\" id=\"tech\">\n" +
    "        <p>More of the sciencey type? Have zero regard for your carbon footprint? Bits+ has an expansive tech tree\n" +
    "            including multiple forms of power generation, a full suite of machinery including the familiar grinder and\n" +
    "            electric furnace, all the way to the electrolysers that make up one of the steps towards making your very\n" +
    "            own nuclear reactor in your backyard! Our tech tree also has a highly configurable fluid, item and power\n" +
    "            transportation system, automatic crop farming and more!</p>\n" +
    "    </div>"

function openSeason(seasonId) {
    let seasonContainer = document.getElementById(seasonId)
    seasonContainer.innerHTML = ""

    fetch('http://localhost.localdomain:5000/statistics_info/' + seasonId).then(response => response.json()).then(seasonData => {
        for (let i = 0; i < seasonData.players.length; i++) {
            let player = seasonData.players[i]

            let playerButton = createPlayerButton(player)
            seasonContainer.appendChild(playerButton)

            let statisticsContainer = createStatisticsContainer(player)

            let statisticsTable = createStatisticsTable()

            for (let j = 0; j < player.statistics.length; j++) {
                let statistic = player.statistics[j]

                let statisticElement = createStatisticElement(statistic)
                statisticsTable.appendChild(statisticElement)
            }

            statisticsContainer.appendChild(statisticsTable)
            seasonContainer.appendChild(statisticsContainer)
        }
    })

    // Display season
    let x = document.getElementsByClassName("season");
    for (let i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    seasonContainer.style.display = "block";
}

function createPlayerButton(player) {
    let playerButton = document.createElement("button")
    playerButton.innerHTML = player.name + "▼"
    playerButton.classList.add("w3-button")
    playerButton.classList.add("w3-block")
    playerButton.classList.add("w3-white")
    playerButton.classList.add("w3-left-align")

    playerButton.setAttribute("onclick", "revealOnAccordion('" + player.uuid + "')")

    return playerButton
}

function createStatisticsTable() {
    let statisticsTable = document.createElement("table")
    statisticsTable.classList.add("w3-table-all")
    statisticsTable.classList.add("statistics-table")

    let statisticsHeaderRow = document.createElement("tr")

    let statisticNameHeader = document.createElement("th")
    statisticNameHeader.innerHTML = "Name"

    let statisticLevelHeader = document.createElement("th")
    statisticLevelHeader.innerHTML = "Level"

    let statisticCountHeader = document.createElement("th")
    statisticCountHeader.innerHTML = "Count"

    statisticsHeaderRow.appendChild(statisticNameHeader)
    statisticsHeaderRow.appendChild(statisticLevelHeader)
    statisticsHeaderRow.appendChild(statisticCountHeader)

    statisticsTable.appendChild(statisticsHeaderRow)

    return statisticsTable
}

function createStatisticElement(statistic) {
    let statisticName = statistic.name
    let statisticLevel = statistic.level
    let statisticCount = statistic.count

    let statisticRow = document.createElement("tr")

    let statisticNameHeader = document.createElement("th")
    statisticNameHeader.innerHTML = statisticName

    let statisticLevelHeader = document.createElement("th")
    statisticLevelHeader.innerHTML = statisticLevel

    let statisticCountHeader = document.createElement("th")
    statisticCountHeader.innerHTML = statisticCount

    statisticRow.appendChild(statisticNameHeader)
    statisticRow.appendChild(statisticLevelHeader)
    statisticRow.appendChild(statisticCountHeader)

    return statisticRow
}

function createStatisticsContainer(player) {
    let statisticsContainer = document.createElement("div")
    statisticsContainer.classList.add("w3-hide")
    statisticsContainer.classList.add("w3-animate-opacity")
    statisticsContainer.classList.add("statistics-container")
    statisticsContainer.style.backgroundColor = "#f1f1f1"

    statisticsContainer.id = player.uuid

    return statisticsContainer
}
