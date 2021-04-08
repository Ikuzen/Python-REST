fetch(
    'http://localhost:5000/api/all',
    {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    }
).then(response => {
    return response.json().then((res)=>{
        console.log(res)
    })
})