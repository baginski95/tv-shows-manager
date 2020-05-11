function init_modal() {
    let modalContainer = document.createElement("div");
    document.body.appendChild(modalContainer);
    modalContainer.classList.add('modal-container');
    let modal = document.createElement('div');
    modalContainer.appendChild(modal);
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

async function populateModalSeasonsList(content) {
    let tvShowName = document.getElementsByClassName("title text-center")[0].textContent;
    let tvShowId = document.getElementById('modalButton').getAttribute('data-show-id');
    let outputContent = `
        <table>
                <thead>
                <tr>
                    <th>Season number</th>
                    <th>overview</th>
                    <th class="action-column">edit/delete</th>
                </tr>
                </thead>
                <tbody>
                `;
    for (let season of content) {
        outputContent += `<tr>
                    <td><a href = "/tv-show/${tvShowId}/${season.id}}?tv_show_name=${tvShowName}">${season.title}</a></td>
                    <td>${season.overview}</td>
                    <td class="action-column">
                        <button type="button" class="icon-button"><i class="fa fa-edit fa-fw"></i></button>
                        <button type="button" class="icon-button"><i class="fa fa-trash fa-fw"></i></button>
                    </td>
                </tr>`
    }
    outputContent += '</tbody></table>';
    document.getElementById('modal').insertAdjacentHTML('afterbegin', outputContent);
    return outputContent
}
let modalButton = document.getElementById('modalButton');
modalButton.addEventListener('click', async (e)=>{
    let contentURL = await e.target.dataset.url;
    let outputContent = await populateModalSeasonsList(await insertContentToModal(init_modal(), contentURL));

});