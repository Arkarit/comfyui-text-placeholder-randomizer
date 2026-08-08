import { app } from "../../../scripts/app.js";

// Locks the node's "preview" widget to read-only and fills it with the
// result text after each execution. Also caps the "text" input widget's
// growable height so that resizing the node vertically only grows the
// preview widget, not both multiline widgets equally (ComfyUI's default
// DOM-widget behavior when a node has more than one growable textarea).
const TEXT_WIDGET_MAX_HEIGHT = 120;

app.registerExtension({
	name: "TextPlaceholderRandomizer.Preview",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if (nodeData.name !== "TextPlaceholderRandomizer") {
			return;
		}

		const onNodeCreated = nodeType.prototype.onNodeCreated;
		nodeType.prototype.onNodeCreated = function () {
			onNodeCreated?.apply(this, arguments);

			const textWidget = this.widgets?.find((w) => w.name === "text");
			if (textWidget?.options) {
				textWidget.options.getMaxHeight = () => TEXT_WIDGET_MAX_HEIGHT;
			}

			const widget = this.widgets?.find((w) => w.name === "preview");
			if (widget?.inputEl) {
				widget.inputEl.readOnly = true;
				widget.inputEl.style.opacity = 0.6;
			}
		};

		const onExecuted = nodeType.prototype.onExecuted;
		nodeType.prototype.onExecuted = function (message) {
			onExecuted?.apply(this, arguments);
			const widget = this.widgets?.find((w) => w.name === "preview");
			if (widget) {
				widget.value = message?.text?.[0] ?? "";
			}
		};
	},
});
