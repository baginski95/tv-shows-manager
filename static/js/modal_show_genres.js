function init_modal() {
    let modal = document.createElement('div');
    document.getElementById("modal-container").appendChild(modal);
    modal.classList.add('modal');
    modal.setAttribute('id', 'modal');
    return modal

}

async function insertContentToModal(modal, contentURL) {
    let response = await fetch(contentURL);
    let json_response = await response.json();
    console.log(json_response);
    return json_response
}

async function populateModalgenres(content) {
    // let tvShowName = document.getElementsByClassName("title text-center")[0].textContent;
    // let tvShowId = document.getElementById('modalButton').getAttribute('data-show-id');

    outputContent
    document.getElementById('modal').insertAdjacentHTML('afterbegin', outputContent);
    return outputContent
}