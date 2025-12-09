document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');
    const form = document.querySelector('form');
    
    if (fileInput && form) {
        // Image preview
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const container = document.querySelector('.container');
                    const existingPreview = document.querySelector('.preview-section');
                    if (existingPreview) existingPreview.remove();
                    
                    container.insertAdjacentHTML('beforeend', `
                        <div class="preview-section">
                            <h3>👁️ Image Preview</h3>
                            <img src="${e.target.result}" style="max-width: 350px; max-height: 350px; border-radius: 12px;">
                            <p><strong>${file.name}</strong><br>
                            Size: ${(file.size/1024).toFixed(1)} KB</p>
                        </div>
                    `);
                }
                reader.readAsDataURL(file);
            }
        });

        // Form validation & loading
        form.addEventListener('submit', function(e) {
            const filterSelect = form.querySelector('select[name="filter"]');
            const button = form.querySelector('button');
            
            if (!filterSelect.value) {
                e.preventDefault();
                alert('⚠️ Please select an AI filter first!');
                return;
            }
            
            button.innerHTML = `🎨 Applying ${filterSelect.options[filterSelect.selectedIndex].text}...`;
            button.disabled = true;
        });
    }
});

