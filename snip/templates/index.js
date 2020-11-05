import Foundation from 'foundation-sites';
import $ from 'jquery';

$("document").ready(() => {
    $(".callout button").on('click', (ev) => showVigour(true));
    $(".input-group-field").one('input', (ev) => showVigour(true));
});

const showVigour = (off) => {
    $(".snip-grid-item").removeClass("hide");
    $(".callout").hide();
};
