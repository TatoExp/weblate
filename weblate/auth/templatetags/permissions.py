# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def perm(context, permission, obj=None):
    return context["user"].has_perm(permission, obj)
