/**
 * Persist changelist filters state (collapsed/expanded).
 */
'use strict';
{
    // Init filters.
    let filters = JSON.parse(sessionStorage.getItem('django.admin.filtersState'));

    if (!filters) {
        filters = {};
    }

    Object.entries(filters).forEach(([key, value]) => {
<<<<<<< HEAD
        const detailElement = document.querySelector(`[data-filter-title='${CSS.escape(key)}']`);
=======
        const detailElement = document.querySelector(`[data-filter-title='${key}']`);
>>>>>>> 84708b22f826d25259fa524313d8417ffbf158c3

        // Check if the filter is present, it could be from other view.
        if (detailElement) {
            value ? detailElement.setAttribute('open', '') : detailElement.removeAttribute('open');
        }
    });

    // Save filter state when clicks.
    const details = document.querySelectorAll('details');
    details.forEach(detail => {
        detail.addEventListener('toggle', event => {
            filters[`${event.target.dataset.filterTitle}`] = detail.open;
            sessionStorage.setItem('django.admin.filtersState', JSON.stringify(filters));
        });
    });
}
