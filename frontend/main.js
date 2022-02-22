window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount()
})

const functionApiUrl = 'https://bs1054test.azurewebsites.net/api/azuretest?code=q9C3dzXtRZu7AKB7OP77qbbJOuQm823GneKFaAryFJDaEUYaw5d4Bg=='
const localfunctionApi = 'http://localhost:7071/api/azuretest'

const getVisitCount = () =>{
    let count = 30
    fetch(functionApiUrl).then(response =>{
        return response.json()
    }).then(response => {
        console.log("Website called function API.")
        count = response.count
        document.getElementById("counter").innerText = count
    }).catch(function(error){
        console.log(error)
    })
    return count
}