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

    let outputContent =`<h2>Genres</h2>`;
    for (let genre of content){
        outputContent += `<p>genre.name</p>`
    }
    document.getElementById('modal').insertAdjacentHTML('afterbegin', outputContent);
    return outputContent
}

function init_genre_modal() {
    let modalLinks = document.getElementsByClassName('modalLinks');
    for (let link of modalLinks ) {
        link.addEventListener('click', async (e) => {
            let contentURL = await e.target.getAttribute('href');
            let outputContent = await populateModalgenres(await insertContentToModal(init_modal(), contentURL));
            let modalContainer = document.getElementById("modal-container");
            modalContainer.classList.add('show-modal');

        });
    }
    window.addEventListener('click', (e)=>{
        let modalContainer = document.getElementById("modal-container");
        if (modalContainer == e.target){
            modalContainer.classList.remove('show-modal');
            modalContainer.innerHTML=''
        }
    })

}
init_genre_modal();