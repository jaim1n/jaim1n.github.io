document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('overflowForm');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const userInput = document.getElementById('userInput').value;
        
        let secondAddressData = "PREDEFINED_DATA";
        
        const firstAddress = userInput.slice(0, 16);
        let secondAddress = userInput.slice(16);
        
        if (secondAddress.length > 0) {
            secondAddressData = secondAddress + secondAddressData.slice(secondAddress.length);
        }
        
        document.getElementById('firstAddress').textContent = firstAddress;
        document.getElementById('secondAddress').textContent = secondAddressData;
    });
});
