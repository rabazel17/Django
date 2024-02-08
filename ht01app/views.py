# ! Создайте пару представлений в вашем первом приложении: главная и о себе.
# ! Внутри каждого представления должна быть переменная html - многострочный текст с HTML вёрсткой и данными о вашем
# первом Django сайте и о вас.
# ! *Сохраняйте в логи данные о посещении страниц

from django.views.generic import TemplateView
import logging

logger = logging.getLogger(__name__)


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        logger.info('Главная страница загружена')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        logger.info('Страница "О себе" загружена')
        context = super().get_context_data(**kwargs)
        context['title'] = 'О себе'
        return context
