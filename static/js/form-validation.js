// Validação de formulários com feedback visual

document.addEventListener('DOMContentLoaded', function() {
    // Função para validar email
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Função para validar telefone (formato brasileiro)
    function isValidPhone(phone) {
        const phoneRegex = /^\(\d{2}\)\s\d{4,5}-\d{4}$|^\d{10,11}$/;
        return phoneRegex.test(phone.replace(/\s/g, ''));
    }

    // Função para adicionar feedback visual
    function addFeedback(input, isValid, message = '') {
        const formGroup = input.closest('.form-group');
        
        // Remove feedback anterior
        const existingFeedback = formGroup.querySelector('.field-feedback');
        if (existingFeedback) {
            existingFeedback.remove();
        }

        // Remove classes anteriores
        input.classList.remove('field-valid', 'field-invalid');
        
        // Adiciona nova classe
        if (isValid) {
            input.classList.add('field-valid');
        } else {
            input.classList.add('field-invalid');
            
            // Adiciona mensagem de erro se fornecida
            if (message) {
                const feedback = document.createElement('div');
                feedback.className = 'field-feedback';
                feedback.textContent = message;
                formGroup.appendChild(feedback);
            }
        }
    }

    // Validação em tempo real para todos os inputs
    const inputs = document.querySelectorAll('input[type="text"], input[type="email"], input[type="password"], input[type="tel"]');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            const value = this.value.trim();
            const fieldName = this.name;
            
            if (value === '') {
                addFeedback(this, false, 'Este campo é obrigatório');
                return;
            }

            switch (fieldName) {
                case 'email':
                    const emailValid = isValidEmail(value);
                    addFeedback(this, emailValid, emailValid ? '' : 'Email inválido');
                    break;
                    
                case 'telefone':
                    const phoneValid = isValidPhone(value);
                    addFeedback(this, phoneValid, phoneValid ? '' : 'Telefone inválido');
                    break;
                    
                case 'senha':
                    const passwordValid = value.length >= 6;
                    addFeedback(this, passwordValid, passwordValid ? '' : 'Senha deve ter pelo menos 6 caracteres');
                    break;
                    
                case 'senha_confirmacao':
                    const senhaInput = document.querySelector('input[name="senha"]');
                    const passwordsMatch = senhaInput && value === senhaInput.value;
                    addFeedback(this, passwordsMatch, passwordsMatch ? '' : 'Senhas não coincidem');
                    break;
                    
                default:
                    const defaultValid = value.length >= 2;
                    addFeedback(this, defaultValid, defaultValid ? '' : 'Mínimo 2 caracteres');
                    break;
            }
        });

        // Validação em tempo real para confirmação de senha
        if (input.name === 'senha_confirmacao') {
            input.addEventListener('input', function() {
                const senhaInput = document.querySelector('input[name="senha"]');
                if (senhaInput && this.value) {
                    const passwordsMatch = this.value === senhaInput.value;
                    addFeedback(this, passwordsMatch, passwordsMatch ? '' : 'Senhas não coincidem');
                }
            });
        }
    });

    // Formatação automática do telefone
    const phoneInput = document.querySelector('input[name="telefone"]');
    if (phoneInput) {
        phoneInput.addEventListener('input', function() {
            let value = this.value.replace(/\D/g, '');
            
            if (value.length <= 11) {
                if (value.length <= 2) {
                    value = value.replace(/(\d{0,2})/, '($1');
                } else if (value.length <= 6) {
                    value = value.replace(/(\d{2})(\d{0,4})/, '($1) $2');
                } else if (value.length <= 10) {
                    value = value.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3');
                } else {
                    value = value.replace(/(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3');
                }
            }
            
            this.value = value;
        });
    }
});

