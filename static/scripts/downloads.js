const masterpageStyle = `background: url("../static/assets/images/downloads/$") no-repeat center center fixed; -webkit-background-size: cover; -moz-background-size: cover; -o-background-size: cover; background-size: cover;`
const initalBackground = "DownloadsBackground.png"


function changeImg(url) {
    document.getElementById("masterpage").style = masterpageStyle.replace("$", url)
}

function resetImg() {
    changeImg(initalBackground)
}

function wd1On() {
    changeImg("112.png");
}

function wd1Off() {
    resetImg()
}

function wd1Redirect() {
    location.href="https://hogwarts.bits.team/world-download/1.12"
}

function wd2On() {
    changeImg("113.png")
}

function wd2Off() {
    resetImg()
}

function wd2Redirect() {
    location.href="https://hogwarts.bits.team/world-download/1.13"
}

function wd3On() {
    changeImg("114.png")
}

function wd3Off() {
    resetImg()
}

function wd3Redirect() {
    location.href="http://hogwarts.bits.team/world-download/1.15"
}

function vResourceOn() {
    changeImg("vanillapack.jpg")
}

function vResourceOff() {
    resetImg()
}

function vResourceRedirect() {
    location.href="https://bits.team/resourcepack"
}

function bResourceOn() {
    changeImg("bitsplus.png")
}

function bResourceOff() {
    resetImg()
}

function bResourceRedirect() {
    location.href="https://hogwarts.bits.team/resources"
}
