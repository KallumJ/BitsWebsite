function addEventToList(name, time, date) {
    let convertedDate = new Date(date.replaceAll("-", "/") + " " + time + " " + "UTC")


    let tableRow = document.createElement("tr")

    let nameElement = document.createElement("th")
    let dateElement = document.createElement("th")
    let timeElement = document.createElement("th")

    let nameText = document.createTextNode(name)
    let dateText = document.createTextNode(convertedDate.toDateString())
    let timeText = document.createTextNode(getTimeString(convertedDate))

    nameElement.appendChild(nameText)
    dateElement.appendChild(dateText)
    timeElement.appendChild(timeText)

    tableRow.appendChild(nameElement)
    tableRow.appendChild(dateElement)
    tableRow.appendChild(timeElement)

    let table = document.getElementById("events-table")
    table.appendChild(tableRow)
}

function getTimeString(date) {
    let hours = date.getHours().toString()
    let minutes = String(date.getMinutes()).padStart(2, "0")
    let timezone = Intl.DateTimeFormat().resolvedOptions().timeZone

    return hours + ":" + minutes + " " + timezone
}