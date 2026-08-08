import { app } from "../../../scripts/app.js";

// Locks the node's "preview" widget to read-only and fills it with the
// result text after each execution.
app.registerExtension({
	name: "TextPlaceholderRandomizer.Preview",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if (nodeData.name !== "TextPlaceholderRandomizer") {
			return;
		}

		const onNodeCreated = nodeType.prototype.onNodeCreated;
		nodeType.prototype.onNodeCreated = function () {
			onNodeCreated?.apply(this, arguments);
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
