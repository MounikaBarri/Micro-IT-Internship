document.getElementById('generateBtn').addEventListener('click', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(document.getElementById('passwordForm'));
    
    const response = await fetch('/generate/', {
        method: 'POST',
        body: formData
    });
    
    const data = await response.json();
    document.getElementById('passwordOutput').value = data.password;
});