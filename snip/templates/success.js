import $ from 'jquery';
import Foundation from 'foundation-sites';
import ClipboardJS from 'clipboard';
import MotionUI from 'motion-ui';

$("document").ready(() => {
    let clipboard = new ClipboardJS('#copy-url');
    clipboard.on('success', (e) => {
        MotionUI.animateIn('#copied-animation', 'slide-in-up', () => $('#copied-animation').hide());
    });

    $('#reload').click((e) => {
        location.reload();
    });

    $(document).foundation();
    $('.has-tip').foundation();
});



