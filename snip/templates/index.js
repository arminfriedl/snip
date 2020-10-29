import $ from 'jquery';
import { createPopper } from '@popperjs/core';

$("document").ready(() => {
    addInvalidOnInvalid();
    removeInvalidOnChange();

 });

let errorPopper = null;

let addInvalidOnInvalid = () => {
    $("input[type='text']").on('invalid', (ev) => {
        if(ev.target.parentNode) {
            $(ev.target.parentNode).addClass("invalid");
            removeInvalidOnChange();
        }
    });

    if ($('.errors').get(0)) {
        errorPopper = createPopper($('.box > form').get(0), $('.errors').get(0), {
            placement: 'bottom',
            modifiers: [
                { name: 'offset', options: { offset: [0, 8]}}
            ]
        });
    }
};

let removeInvalidOnChange = () => {
    $("input[type='text']").one('input', (ev) => {
        if(ev.target.parentNode) {
            $(ev.target.parentNode).removeClass("invalid");
        }

        if (errorPopper) {
            errorPopper.destroy();
            errorPopper = null;
        }
    });
};
