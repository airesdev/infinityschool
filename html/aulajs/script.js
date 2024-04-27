const form = document.querySelector("#form")
const cepInput = document.querySelector("#cepInput")
const section = document.querySelector("#section")
const message = document.querySelector("#message")

document.addEventListener("submit", (e)=>{
    e.preventDefault()
    const link = "https://viacep.com.br/ws/" + cepInput.value + "/json/"
    // console.log(link)
    buscarCep(link)
})

// fetch => asincrona => async
async function buscarCep(link){

    // try => tentar
    try{
        const requisition = await fetch(link)
        const resposta = await requisition.json()

        // backend specific
        if(resposta.erro){
            message.textContent = "CEP Inválido"
        }else{
            showCep(resposta)
        }
    }catch(error){
        console.log(error)
        console.log("the API triped on a rock and fell, oops...")
    }
}

function showCep(json){
    const cep = document.createElement("h1")
    cep.textContent = json.cep

    const logradouro = document.createElement("p")
    logradouro.textContent = `Endereço: ${json.logradouro}`
    section.appendChild(logradouro)

    const complemento = document.createElement("p")
    complemento.textContent = `Complemento: ${json.complemento}`
    section.appendChild(complemento)

    const bairro = document.createElement("p")
    bairro.textContent = `Bairro: ${json.bairro}`
    section.appendChild(bairro)

    const localidade = document.createElement("p")
    localidade.textContent = `Localidade: ${json.localidade}`
    section.appendChild(localidade)
}

// get - solicitar
// post - enviar
// delete - \<- _->/
// patch - atualizar

// CRUD, CREATE, READ, UPDATE, DELETE