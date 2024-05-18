async function buscarCep(){
    try{
        const requisicao = await fetch("")
        const resposta = await requisicao.json()
        console.log(resposta)

        // específico da api
        if(resposta.erro){
            console.log("CEP inválido")
        }
    }catch(error){
        console.log("Error na API")
    }
}