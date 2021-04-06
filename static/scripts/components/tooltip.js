function copied(ip) {
    // Create new element
    const el = document.createElement('textarea')

    // Set value (string to be copied)
    el.value = ip

    // Set non-editable to avoid focus and move outside of view
    el.setAttribute('readonly', '')
    el.style = {position: 'absolute', left: '-9999px'}
    document.body.appendChild(el)

    // Select text inside element
    el.select()

    // Copy text to clipboard
    document.execCommand('copy')

    // Remove temporary element
    document.body.removeChild(el)

    // Set the tooltip text
    this.tooltipText = 'Copied!'

    const tooltip = document.querySelector("[data-tooltip]")
    tooltip.setAttribute("data-tooltip", "Copied!")

    // Reset tooltip
    setTimeout(() => {
        tooltip.setAttribute("data-tooltip", "Click to Copy!")
    }, 5000)
}