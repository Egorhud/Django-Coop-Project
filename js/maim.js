// Простая навигация (пока что заглушки)
function navigateTo(section) {
    switch(section) {
        case 'forum':
            alert('Переход в раздел Форум (в разработке)');
            break;
        case 'tasks':
            alert('Переход в раздел Задачи (в разработке)');
            break;
        case 'calendar':
            alert('Переход в раздел Календарь (в разработке)');
            break;
        case 'profile':
            alert('Переход в Профиль (в разработке)');
            break;
        default:
            console.log('Неизвестный раздел:', section);
    }
}

// Плавная анимация при загрузке
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 150);
    });
});

// Эффект параллакса для фона
document.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    const rate = scrolled * -0.5;
    document.body.style.backgroundPosition = `center ${rate}px`;
    